from pathlib import Path

from analyzer.process_text import extract_words
from analyzer.statistics import get_most_frequent, calculate_statistics

from collections import Counter
import pandas as pd

def read_work(path: Path) -> tuple[int, list[str]]:
    text = path.read_text(encoding="utf-8")

    lines = len(text.splitlines())
    words = extract_words(text)

    return lines, words

def read_works(paths: list[Path]) -> dict[Path, tuple[int, list[str]]]:
    return {path: read_work(path) for path in paths}

def calculate_work_statistics(num_lines: int, words: list[str]) -> dict:
    return calculate_statistics(num_lines, words)

def calculate_total_statistics(works: dict[Path, tuple[int, list[str]]]) -> dict:
    total_lines = 0
    total_words = []

    for lines, words in works.values():
        total_lines += lines
        total_words.extend(words)

    return calculate_statistics(total_lines, total_words)

def get_work_frequencies(works: dict[Path, tuple[int, list[str]]], limit: int) -> dict[Path, list[tuple[str, int]]]:
    return {path: get_most_frequent(words, limit) for path, (_, words) in works.items()}

def compare_works(works: dict[Path, tuple[int, list[str]]]) -> pd.DataFrame:
    names = [path.name for path in works]
    frequencies = {path.name: Counter(words) for path, (_, words) in works.items()}

    num_words = {path.name: len(words) for path, (_, words) in works.items()}

    vocabulary = sorted({word for _, words in works.values() for word in words})

    frequency_frame = pd.DataFrame(
        {name: [frequencies[name][word] / num_words[name] if num_words[name] > 0 else 0 for word in vocabulary] for name in names},
        index=vocabulary
    )

    scores = pd.DataFrame(0.0, index = names, columns = names)

    for first in names:
        for second in names:
            num = float( (frequency_frame[first] * frequency_frame[second]).sum() )
            denom = float( (frequency_frame[first].pow(2).sum() * frequency_frame[second].pow(2).sum()) ** 0.5 )

            if denom != 0:
                scores.loc[first, second] = (100 * num / denom)
    return scores