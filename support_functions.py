import sys
import os
import time
import math


COMMON_LEN_IDX = 4


def open_file(filename, encoding="utf-8"):
    if os.path.exists(filename):
        file_encoding = encoding if encoding else "utf-8"
        try:
            with open(filename, encoding=file_encoding) as fin:
                text_document_lines = fin.readlines()
        except UnicodeError:
            print("Возникла ошибка, свзяанная с кодировкой файла")
            sys.exit(0)
        else:
            return text_document_lines
    else:
        print("Входной файл не был найден")
        sys.exit(0)


def write_file(content, filename, encoding="utf-8"):
    try:
        with open(filename, encoding=encoding, mode="w") as file_out:
            file_out.write(content)
    except UnicodeError:
        print("Возникла ошибка при записи выходного файла")


def progressbar(current, total, label="Progress", suffix="█"):
    percentage = round((current/total)*100, 1)
    line_length = int((percentage - percentage % 10) // 10)
    sys.stdout.write("{}: {}% |{}|\r".format(label, percentage, line_length*suffix*COMMON_LEN_IDX + (10 - line_length)*" "*COMMON_LEN_IDX))
    sys.stdout.flush()



