import os

from module1.reader.compressed import gzipped, bzipped

EXTENSION_MAP = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener
}


class Reader(object):

    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        opener = EXTENSION_MAP.get(extension, open)
        self.file = opener(filename, 'rt')

    def close(self):
        self.file.close()

    def read(self):
        return self.file.read()
