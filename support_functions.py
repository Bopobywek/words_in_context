import sys
import os


COMMON_LEN_IDX = 4
MAX_LINE_LENGTH = 10
TEMPLATE = "Found word \"{}\" in {} line. In following context: \"...{}...\""


def open_file(filename, encoding="utf-8"):
    if os.path.exists(filename):
        file_encoding = encoding if encoding else "utf-8"
        try:
            with open(filename, encoding=file_encoding) as fin:
                text_document_lines = fin.readlines()
        except UnicodeDecodeError:
            raise UnicodeDecodeError("Invalid encoding. Please, specify encoding with -enc parameter")
        else:
            return text_document_lines
    else:
        raise ValueError("Wrong path to file. Not found")


def write_file(content, filename, encoding="utf-8"):
    try:
        with open(filename, encoding=encoding, mode="w") as file_out:
            for element in content:
                file_out.write("{}\n".format(element))
    except Exception as e:
        raise IOError("Error! Cannot write file")


def prepare_matches_to_output(matches, lines, amount_of_strings=None):
    matches_length_before = len(matches)
    result = ["Found {} matches".format(matches_length_before)]
    matches = matches if not amount_of_strings else matches[:amount_of_strings]
    result.append("Printed {} matches".format(len(matches)))
    for word, word_idx, line_idx in matches:
        original_line = lines[line_idx]
        if word_idx <= 2 and line_idx == 0:
            string = TEMPLATE.format(word, line_idx + 1, original_line)
        elif word_idx <= 2 and line_idx != 0:
            previous_line = lines[line_idx - 1]
            string = TEMPLATE.format(word, line_idx + 1, " ".join(previous_line.split()[-2:]) +
                                     " " + " ".join(original_line.split()[:word_idx + 2]))
        else:
            string = TEMPLATE.format(word, line_idx + 1, " ".join(original_line.split()[word_idx - 2: word_idx + 2]))
        result.append(string)
    return result


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

