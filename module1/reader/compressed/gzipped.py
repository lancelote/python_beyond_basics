import gzip
import sys

opener = gzip.open

if __name__ == '__main__':
    file = gzip.open(sys.argv[1], mode='wt')
    file.write(' '.join(sys.argv[2:]))
    file.close()
