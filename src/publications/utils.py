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


def parse_infoscience(url):
    """read content from given url, which can be either an http or file one"""
    logger.info("Fetching %s", url)
    content = urlopen(url)

    old_id = 0
    count = 0

    authors_list = []
    for line in content:
        logging.debug("Parsing line %s", line)
        current_id = line[:9]

        if current_id != old_id:  # New record
            if count != 0:
                p.save()
                for author in authors_list:
                    p.authors.add(author)
                authors_list = []

            p = Publication()
            count += 1
        else:  # Same record
            nb = line[10:15]

            if b'245' in nb:  # Title
                p.title = line[19:-1]
            elif b'700' in nb:  # Author
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

                authors_list.append(author)
            elif b'0247' in nb:  # DOI
                p.doi = line[25:-1]
            elif b'260' in nb:  # Publication year
                line = line.decode('utf-8')
                pos = line.find('$$c')

                if pos != -1:
                    p.pub_date = line[pos + 3:pos + 3 + 4]

        old_id = current_id

    logger.info("Fetched %d records", count)


def parse_wos(req, debug=False):
    if not debug:
        with WosClient(lite=True) as client:
            res = wos.utils.query(client, req, count=2, limit=1)

        print(res)

        root = ET.fromstring(res)
    else:
        tree = ET.parse('ex_wos.xml')
        root = tree.getroot()

    publications = []

    for title in root.iter('title'):
        p = Publication()
        p.title = title[1].text
        publications.append(p)

    count = 0
    for authors in root.iter('authors'):
        authors_list = []
        for author in authors:
            if author.text != 'Authors':
                comma_pos = author.text.find(',')
                a = Author(
                    name=author.text[comma_pos + 2:],
                    surname=author.text[:comma_pos]
                )
                authors_list.append(a)
        publications[count].authors_list = authors_list
        count += 1

    count = 0
    for source in root.iter('source'):
        if source[0].text == 'Published.BiblioYear':
            publications[count].pub_date = int(source[1].text)
            count += 1

    count = 0
    for other in root.iter('other'):
        if other[0].text == 'Identifier.Xref_Doi':
            publications[count].doi = other[1].text
            count += 1

    c = Comparator()
    for pub in publications:
        check = c.check(pub)
        if check[0] == -1:
            pub.save()
            for a in pub.authors_list:
                au, created = Author.objects.get_or_create(
                    name=a.name,
                    surname=a.surname
                )
                pub.authors.add(au)

            logger.info("Added publication: %s (%s)" % (pub.title, pub.doi))


class Comparator:
    SAME_DOI = 1
    SAME_TITLE_SAME_AUTHORS = 2
    SAME_TITLE_DIFFERENT_AUTHORS = 3
    NO_SIMILAR_TITLE = 4
    NO_DOI_AND_TITLE = 5
    DOI_NOT_FOUND = 6
    SAME_TITLE_SAME_YEAR_SAME_AUTHORS = 7
    SAME_TITLE_DIFFERENT_YEARS = 8
    SAME_TITLE_SAME_YEAR_DIFFERENT_AUTHORS = 9

    # Returns:  -1  if publication doesn't exist
    #           0   if not sure
    #           1   if publication already exists
    def check(self, publication):
        if hasattr(publication, 'doi') and publication.doi is not None:
            try:
                p = Publication.objects.get(doi=publication.doi)
                return 1, self.SAME_DOI, p.id
            except Publication.DoesNotExist:
                return -1, self.DOI_NOT_FOUND

        if hasattr(publication, 'title'):
            publications = Publication.objects.all()

            for p2 in publications:
                if similar(publication.title, p2.title) >= .95:
                    if publication.pub_date == p2.pub_date:
                        if publication.authors_list == p2.authors:
                            return 1, self.SAME_TITLE_SAME_YEAR_SAME_AUTHORS, p2.id
                        else:
                            return 0, self.SAME_TITLE_SAME_YEAR_DIFFERENT_AUTHORS, p2.id
                    else:
                        return 0, self.SAME_TITLE_DIFFERENT_YEARS, p2.id

            return -1, self.NO_SIMILAR_TITLE

        return 0, self.NO_DOI_AND_TITLE
