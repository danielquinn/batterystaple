import hashlib
import re

try:
    # Python3
    from urllib.request import Request, urlopen
except ImportError:
    # Python2
    from urllib2 import urlopen, Request

class Password(object):

    SEARCH = "https://www.google.ca/search?q={}"

    def __init__(self, password):
        self.cleartext = password

    def check_rainbow(self, lib):

        digest = getattr(hashlib, lib)(self.cleartext.encode("utf-8"))
        hexdigest = digest.hexdigest()
        url = self.SEARCH.format(hexdigest)

        response = urlopen(
            Request(url, headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux i586; rv:34.0) "
                              "Gecko/20100101 Firefox/31.0"
            })
        )

        not_found = "Your search - <em>{}</em> - did not match any documents".format(
            hexdigest
        )
        if not_found in str(response.read()):
            return False
        return True

    def check_rainbows(self):
        for lib in ("md5", "sha1", "sha256"):
            if not self.check_rainbow(lib):
                return False
        return True
