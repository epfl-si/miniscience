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
                a = Author(name=line[19:-1])
                # a.save()
                # p.authors.add(a)
            elif b'0247' in nb:  # DOI
                p.doi = line[25:-1]

        old_id = current_id

    logging.info("Fetched %d records", count)
