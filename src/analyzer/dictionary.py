from pathlib import Path

from analyzer.statistics import calculate_statistics

def read_dictionary(path: Path) -> tuple[int, list[str]]: # Read dictionary - return (number of lines, all words forms)
    lines = path.read_text(encoding="utf-8").splitlines()

    words = []
    for line in lines:
        forms = line.split(",")
        for word in forms:
            word = word.strip().lower()
            if word:
                words.append(word)

    return len(lines), words


def calculate_dictionary_statistics(num_lines: int, words: list[str]) -> dict: # return statistics for dictionary
    return calculate_statistics(num_lines, words)
    