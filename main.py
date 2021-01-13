import sys
import os

import argparse

from support_functions import open_file, write_file, progressbar,\
    prepare_matches_to_output, print_to_console
from morph import normalize_word


def find_word(lines, word_to_find, verbose=True):

    """
    :param lines: list
    :param word_to_find: str
    :param verbose: bool
    :return: matches: list of tuples. Each tuple has the following structure:
     (match, index of match in the line, index of line)
    """

    matches = []
    normalized_word_to_find = normalize_word(word_to_find)
    text_length = len(lines)
    for line_idx, line_content in enumerate(lines):

        normalized_words = []
        for word_idx, word in enumerate(line_content):
            normalized_word = normalize_word(word)
            if word:
                normalized_word.append((word_idx, normalized_words))
        for word_idx, word in normalized_words:
            if word == normalized_word_to_find:
                matches.append((line_content[word_idx], word_idx, line_idx))
        if verbose:
            progressbar(line_idx + 1, text_length, label="Progress of text analysis")

    return matches


def main():
    parser = argparse.ArgumentParser(description='Without description')

    parser.add_argument('file_in', action="store", help="path to text file")
    parser.add_argument('word_to_find', action="store", help="word to find")
    parser.add_argument('-i', action="store", dest="file_in", required=False, help="Path to text file")
    parser.add_argument('-w', action="store", dest="word_to_find", required=False, help="Word to find")
    parser.add_argument('-enc', action="store", dest="encoding", required=False, default="utf-8",
                        help="Encoding of input file")
    parser.add_argument('-v', action="store", dest="verbose", default=True,
                        help="Prints the program status to the console", type=bool)
    parser.add_argument('-o', action="store", dest="file_out", default="",
                        help="Path to output file. If not specified, the utility prints output to the stdout")
    parser.add_argument('-n', action="store", dest="amount_of_strings",
                        default=10, type=int, help="Amount of strings to output")

    args = parser.parse_args()

    lines = open_file(filename=args.file_in)
    matches = find_word(lines, args.word_to_find)
    result = prepare_matches_to_output(matches, args.amount_of_strings)
    if args.file_out:
        write_file(result, args.file_out, args.encoding)
    else:
        print_to_console(result)


if __name__ == '__main__':
    main()
