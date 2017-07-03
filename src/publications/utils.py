import logging
from difflib import SequenceMatcher

from wos import WosClient
import wos.utils
import xml.etree.ElementTree as ET

from .models import Publication, Author

logger = logging.getLogger(__name__)

try:
    # python 3
    from urllib.request import urlopen
except ImportError:
    # python 2.7
    from urllib2 import urlopen


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def do_request(url):
    """read content from given url, which can be either an http or file one"""
    logger.info("Fetching %s", url)
    content = urlopen(url)

    old_id = 0
    count = 0

    for line in content:
        logging.debug("Parsing line %s", line)
        current_id = line[:9]

        if current_id != old_id:  # New record
            if count != 0:
                p.save()

            p = Publication()
            count += 1
        else:  # Same record
            nb = line[10:15]

            if b'245' in nb:  # Title
                p.title = line[19:-1]
            elif b'700' in nb:  # Author
                p.save()

                line = line.decode('utf-8')
                comma = line.find(',')
                surname = line[19:comma]
                name = line[comma + 2:]
                useless_begins = name.find('$$')
                sciper_begins = name.find('$$g')

                if sciper_begins != -1:
                    sciper = name[sciper_begins + 3: sciper_begins + 3 + 6]
                else:
                    sciper = -1

                if useless_begins != -1:
                    name = name[:useless_begins]
                else:
                    name = name[:-1]

                author, created = Author.objects.get_or_create(
                    name=name,
                    surname=surname
                )

                if created and sciper != -1:
                    author.sciper = sciper
                    author.save()

                p.authors.add(author)
            elif b'0247' in nb:  # DOI
                p.doi = line[25:-1]
            elif b'260' in nb:  # Publication year
                line = line.decode('utf-8')
                pos = line.find('$$c')

                if pos != -1:
                    p.pub_date = line[pos + 3:pos + 3 + 4]

        old_id = current_id

    logger.info("Fetched %d records", count)


def parse_wos(req):
    with WosClient(lite=True) as client:
        res = wos.utils.query(client, req, count=2, limit=1)

    print(res)

    root = ET.fromstring(res)

    for title in root.iter('title'):
        title = title[1].text

    authors_list = []
    for authors in root.iter('authors'):
        for author in authors:
            if author.text != 'Authors':
                comma_pos = author.text.find(',')
                a, created = Author.objects.get_or_create(
                    name=author.text[comma_pos + 2:],
                    surname=author.text[:comma_pos]
                )
                authors_list.append(a)

    for source in root.iter('source'):
        if source[0].text == 'Published.BiblioYear':
            year = int(source[1].text)

    for other in root.iter('other'):
        if other[0].text == 'Identifier.Xref_Doi':
            doi = other[1].text

    p = Publication(title=title, pub_date=year, doi=doi)
    p.save()

    for author in authors:
        p.authors.add(author)

    print('Title: %s\nYear: %d\nDOI: %s\nAuthors: %s' % (title, year, doi, authors_list))

    logger.info("Added publication: %s (%s)" % (title, doi))


class Comparator:
    SAME_DOI = 1
    SAME_TITLE_SAME_AUTHORS = 2
    SAME_TITLE_DIFFERENT_AUTHORS = 3
    NO_SIMILAR_TITLE = 4
    NO_DOI_AND_TITLE = 5

    # Returns:  -1  if publication doesn't exist
    #           0   if not sure
    #           1   if publication already exists
    def check(self, publication):
        if hasattr(publication, 'doi'):
            try:
                Publication.objects.get(doi=publication.doi)
            except Publication.DoesNotExist:
                return 1, self.SAME_DOI

        if hasattr(publication, 'title'):
            publications = Publication.objects.all()

            for p2 in publications:
                if similar(publication.title, p2.title) >= .9:
                    if publication.authors == p2.auhors:
                        return 1, self.SAME_TITLE_SAME_AUTHORS
                    else:
                        return 0, self.SAME_TITLE_DIFFERENT_AUTHORS

            return -1, self.NO_SIMILAR_TITLE

        return 0, self.NO_DOI_AND_TITLE
