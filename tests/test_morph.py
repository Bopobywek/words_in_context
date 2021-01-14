import unittest

from morph import remove_punctuation_from_word, normalize_word


class MorphTest(unittest.TestCase):

    def test_dots(self):
        self.assertEqual(remove_punctuation_from_word("Да..."), "Да")

    def test_languages(self):
        self.assertEqual(remove_punctuation_from_word("Ну!!!..."), "Ну")
        self.assertEqual(remove_punctuation_from_word("How?!"), "How")
        self.assertEqual(remove_punctuation_from_word("ワークス!"), "ワークス")

    def test_do_nothing(self):
        self.assertEqual(remove_punctuation_from_word("Ничего"), "Ничего")
        self.assertEqual(remove_punctuation_from_word("Определенно"), "Определенно")
        self.assertNotEqual(remove_punctuation_from_word("Ага"), "ага")

    def test_from_normalize(self):
        self.assertEqual(normalize_word("Будет"), "быть")
        self.assertEqual(normalize_word("Покушали"), "покушать")
        self.assertEqual(normalize_word("Игрушечное"), "игрушечный")
        self.assertEqual(normalize_word("Меня"), "я")
        self.assertEqual(normalize_word("двух"), "два")


if __name__ == '__main__':
    unittest.main()
