from collections import Counter

POLISH_LETTERS = set("aąbcćdeęfghijklłmnńoóprsśtuwyzźż")

def sort_elements(elems: Counter) -> list[tuple[str, int]]: # sorting first descending, then in alphabetical order
    return sorted(elems.items(), key = lambda item: (-item[1], item[0]))

def get_most_frequent(words: list[str], limit: int = 10) -> list[tuple[str, int]]: # return most frequent words (with ties at the limit)
    sorted_words = sort_elements(Counter(words))

    if len(sorted_words) <= limit:
        return sorted_words

    corrected_limit = sorted_words[limit-1][1]

    return [(word, count) for word, count in sorted_words if count >= corrected_limit]

def count_characters(words: list[str]) -> tuple[list[tuple[str, int]], list[tuple[str, int]]]: # return polish and other characters with its counters
    polish_letters = Counter()
    other_characters = Counter()

    for word in words:
        for character in word:
            if character in POLISH_LETTERS:
                polish_letters[character] += 1
            else:
                other_characters[character] += 1

    return (sort_elements(polish_letters), sort_elements(other_characters))

def calculate_statistics(num_lines: int, words: list[str]) -> dict: # return statistics for dictionary
    unique_num_words = Counter(words)
    polish_letters, other_characters = count_characters(words)

    return {
        "num_lines": num_lines,
        "num_words": len(words),
        "unique_num_words": len(unique_num_words),
        "top_words": get_most_frequent(words),
        "polish_letters": polish_letters,
        "other_characters": other_characters
    }