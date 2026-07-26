from pathlib import Path

from analyzer.process_text import extract_words
from analyzer.statistics import calculate_statistics

def read_work(path: Path) -> tuple[int, list[str]]:
    text = path.read_text(encoding="utf-8")

    lines = len(text.splitlines())
    words = extract_words(text)

    return lines, words

def read_works(paths: list[Path]) -> dict[Path, tuple[int, list[str]]]:
    return {path: read_work(path) for path in paths}

def calculate_work_statistics(num_lines: int, words: list[str]) -> dict:
    return calculate_statistics(num_lines, words)