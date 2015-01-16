import hashlib
import re

from urllib.request import Request, urlopen


class Password(object):

    DICTIONARIES = ("/usr/share/dict/words", "/usr/share/dict/extra.words")
    SEARCH = "https://www.google.nl/search?q={}"

    def __init__(self, password, min_length=20):

        self.minimum_length = min_length

        self.cleartext = password

    def check_length(self):
        return len(self.cleartext) > self.minimum_length

    def check_dictionary(self):

        words = []
        for dictionary in self.DICTIONARIES:
            with open(dictionary) as f:
                words += [word.strip() for word in f.readlines()]

        if self.cleartext in words:
            return False

        return True

    def check_rainbow(self, lib):

        digest = getattr(hashlib, lib)(self.cleartext.encode("utf-8"))
        url = self.SEARCH.format(digest.hexdigest())

        request = Request(url, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux i586; rv:34.0) Gecko/20100101 Firefox/31.0"
        })

        if self.cleartext in str(urlopen(request).read()):
            return False

        return True

    def check_rainbows(self):
        for lib in ("md5", "sha1", "sha256"):
            if not self.check_rainbow(lib):
                return False
        return True
