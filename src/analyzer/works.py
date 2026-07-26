"""
works.py
├── read one work text file
├── split its text into words
└── return the extracted words
"""

from pathlib import Path

from analyzer.process_text import extract_words

def read_work(path: Path) -> tuple[int, list[str]]:
    text = path.read_text(encoding="utf-8")

    lines = len(text.splitlines())
    words = extract_words(text)

    return lines, words