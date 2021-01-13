from pymorphy2 import MorphAnalyzer


morph_analyzer = MorphAnalyzer()


def normalize_word(word):
    word = [symbol.lower() for symbol in word if symbol.isalpha()]
    if not word:
        return ""
    variants = morph_analyzer.parse(word)
    if not variants:
        return ""
    word_in_normal_form = variants[0].normal_form
    return word_in_normal_form
