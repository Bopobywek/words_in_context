from pymorphy2 import MorphAnalyzer


morph_analyzer = MorphAnalyzer()


def remove_punctuation(word):
    return "".join([symbol for symbol in word if symbol.isalpha()])


def normalize_word(word):
    word = remove_punctuation(word)
    if not word:
        return ""
    variants = morph_analyzer.parse(word)
    if not variants:
        return ""
    word_in_normal_form = variants[0].normal_form
    return word_in_normal_form
