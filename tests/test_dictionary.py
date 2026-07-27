from pathlib import Path

from analyzer.dictionary import read_dictionary, calculate_dictionary_statistics

def test_read_dictionary():
    lines, words = read_dictionary(Path("data/odm.txt"))

    assert lines > 0
    assert len(words) > 0

def test_dictionary_statistics():
    lines, words = read_dictionary(Path("data/odm.txt"))
    stats = calculate_dictionary_statistics(lines, words)

    assert stats["num_lines"] == lines
    assert stats["num_words"] == len(words)