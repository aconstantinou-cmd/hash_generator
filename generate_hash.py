import argparse
import hashlib
import os
import sys


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="filename", help="file to be hashed")
    args = parser.parse_args()
    return args


def sha1_hash(filename):
    if os.path.isfile(filename):
        sha1 = hashlib.sha1()
        with open(filename, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha1.update(chunk)
        return sha1.hexdigest()
    else:
        print("File not found")
        sys.exit(1)


def md5_hash(filename):
    if os.path.isfile(filename):
        md5 = hashlib.md5()
        with open(filename, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                md5.update(chunk)
        return md5.hexdigest()
    else:
        print("File not found")
        sys.exit(1)


def sha256_hash(filename):

    if os.path.isfile(filename):
        sha256 = hashlib.sha256()
        with open(filename, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    else:
        print("File not found")
        sys.exit(1)


def main():
    args = get_arguments()
    if args.filename:
        print("SHA1:", sha1_hash(args.filename))
        print("MD5:", md5_hash(args.filename))
        print("SHA256:", sha256_hash(args.filename))
    else:
        print("No file specified")
        sys.exit(1)


if __name__ == '__main__':
    main()
