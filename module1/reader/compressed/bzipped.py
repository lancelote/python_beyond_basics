import bz2
import sys

opener = bz2.open

if __name__ == '__main__':
    file = bz2.open(sys.argv[1], mode='wt')
    file.write(' '.join(sys.argv[2:]))
    file.close()
