import logging

from .models import Publication, Author

try:
    # python 3
    from urllib.request import urlopen
except ImportError:
    # python 2.7
    from urllib2 import urlopen


def do_request(url):
    """read content from given url, which can be either an http or file one"""
    logging.info("Fetching %s", url)
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
                name = line[comma+2:]
                useless_begins = name.find('$$')
                sciper_begins = name.find('$$g')

                if sciper_begins != -1:
                    sciper = name[sciper_begins+3: sciper_begins+3+6]
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
                    p.pub_date = line[pos+3:pos+3+4]

        old_id = current_id

    logging.info("Fetched %d records", count)
