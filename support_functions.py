import sys
import os


COMMON_LEN_IDX = 4
MAX_LINE_LENGTH = 10


def open_file(filename, encoding="utf-8"):
    if os.path.exists(filename):
        file_encoding = encoding if encoding else "utf-8"
        try:
            with open(filename, encoding=file_encoding) as fin:
                text_document_lines = fin.readlines()
        except UnicodeError:
            print("Invalid encoding. Please, specify encoding with -enc parameter")
            sys.exit(0)
        else:
            return text_document_lines
    else:
        print("Wrong path to file. Not found")
        sys.exit(0)


def write_file(content, filename, encoding="utf-8"):
    try:
        with open(filename, encoding=encoding, mode="w") as file_out:
            file_out.write(content)
    except UnicodeError:
        print("Error! Cannot write file")


def prepare_matches_to_output(matches, amount_of_strings=None):
    pass


def print_to_console(content):
    for string in content:
        print(string)


def progressbar(current, total, label="Progress", suffix="█"):
    percentage = round((current/total)*100, 1)
    line_length = int((percentage - percentage % 10) // MAX_LINE_LENGTH)
    template = "{}: {}% |{}|\r".format(
        label, percentage, line_length*suffix*COMMON_LEN_IDX + (MAX_LINE_LENGTH - line_length)*" "*COMMON_LEN_IDX)
    sys.stdout.write(template)
    sys.stdout.flush()
    if line_length == MAX_LINE_LENGTH:
        sys.stdout.write("{}\r".format(" "*len(template)))
        sys.stdout.flush()

