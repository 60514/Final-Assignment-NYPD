from analyzer.analysis import find_unknown_words

def test_unknown_words():
    dictionary = {"ala", "ma"}

    words = [
        "ala",
        "ma",
        "kota",
        "kota",
        "pies"
    ]

    unknown = find_unknown_words(words, dictionary)

    assert ("kota", 2) in unknown
    assert ("pies", 1) in unknown