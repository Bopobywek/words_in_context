import os
import unittest

from support_functions import open_file, write_file, prepare_matches_to_output
from main import find_word


class TestIO(unittest.TestCase):

    def test_file_read(self):
        self.assertRaises(ValueError, open_file, "this_file_maybe_exist.txt")
        self.assertEqual(open_file("../texts/text1.txt"), ["Тест был написан 13 января в 22:54 :))))\n"])
        self.assertRaises(UnicodeError, open_file, "../texts/test.txt")

    def test_file_write(self):
        self.assertRaises(OSError, write_file, "Не хватает прав на запись:(", "/tmp/iam_root.txt")
        write_file("Буковки", "../texts/test2.txt")
        self.assertIn("test2", os.listdir("../texts"))

    def test_preparing_matches(self):
        word_to_find = "слово"
        lines = ["раз, два, три"]
        result = prepare_matches_to_output(find_word(lines, word_to_find, verbose=False), lines)
        self.assertIsInstance(result, list)
        self.assertEqual(result, ['Found 0 matches', 'Printed 0 matches'])

        word_to_find = "три"
        lines = ["раз, два, три"]
        result = prepare_matches_to_output(find_word(lines, word_to_find, verbose=False), lines)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)


if __name__ == '__main__':
    unittest.main()
