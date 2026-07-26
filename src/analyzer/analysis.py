# Statistics that need both dictionary and works

from collections import Counter

from analyzer.statistics import sort_elements

def find_unknown_words(work_words: list[str], dictionary_words: list[str]) -> list[tuple[str, int]]:
    dictionary_set = set(dictionary_words)

    unknown_word_counts = Counter()

    for word in work_words:
        if word not in dictionary_set:
            unknown_word_counts[word] += 1

    return sort_elements(unknown_word_counts)