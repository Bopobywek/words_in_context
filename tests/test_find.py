import unittest

from main import find_word
from support_functions import prepare_matches_to_output, write_file


class TestFind(unittest.TestCase):

    def test_empty_result(self):
        word_to_find = "слово"
        lines = ["раз, два, три"]
        result = prepare_matches_to_output(find_word(lines, word_to_find, verbose=False), lines)
        write_file(result, "empty_result_text.txt")
        with open("empty_result_text.txt") as check_file:
            self.assertEqual(check_file.read(), "Found 0 matches\nPrinted 0 matches\n")

    def test_result(self):
        word_to_find = "дождливый"
        lines = ["По-моему, это произошло очень давно...",
                 "Тогда был дождливый день, а настроение, по понятным причинам, оставляло желать лучшего"]
        result = prepare_matches_to_output(find_word(lines, word_to_find, verbose=False), lines)
        write_file(result, "result_text.txt")
        with open("result_text.txt") as check_file:
            matches = check_file.read()
            self.assertEqual("дождливый" in matches, True)


if __name__ == '__main__':
    unittest.main()
