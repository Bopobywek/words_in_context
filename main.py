import sys
import os

import argparse


def main():
    parser = argparse.ArgumentParser(description='Without description')
    parser.add_argument('file_in', action="store", help="text file")
    parser.add_argument('word_to_find', action="store", help="word to find")
    parser.add_argument('-i', action="store", dest="file_in", required=False)
    parser.add_argument('-w', action="store", dest="word_to_find", required=False)
    parser.add_argument('-enc', action='store', dest="encoding", required=False)
    parser.add_argument('-v', action="store", dest="verbose", default=True)
    parser.add_argument('-o', action="store", dest="file_out", default=True)
    parser.add_argument('-n', action="store", dest="number_of_strings", default=10, type=int)

    args = parser.parse_args()


if __name__ == '__main__':
    main()
