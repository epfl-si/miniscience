import logging
from datetime import datetime

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
    p = Publication(timestamp=datetime.now().timestamp())

    for line in content:
        logging.debug("Parsing line %s", line)
        current_id = line[:9]

        if current_id != old_id:  # New record
            p.save()
            p = Publication(timestamp=datetime.now().timestamp())
            count += 1
        else:  # Same record
            nb = line[10:13]

            if nb == b'245':  # Title
                p.title = line[19:-1]
            elif nb == b'700':  # Author
                p.save()
                a = Author(first_name=line[19:-1])
                a.save()
                p.author.add(a)

        old_id = current_id

    logging.info("Fetched %d records", count)
