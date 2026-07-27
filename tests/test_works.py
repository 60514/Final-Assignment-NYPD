from pathlib import Path

from analyzer.works import read_work, read_works, calculate_work_statistics, compare_works

def test_read_work():
    lines, words = read_work(Path("data/Pan_Tadeusz.txt"))

    assert lines > 0
    assert len(words) > 0

def test_read_works():
    works = read_works([
        Path("data/Pan_Tadeusz.txt"),
        Path("data/Pan_Tedeusz.txt")
    ])

    assert len(works) == 2

def test_work_statistics():
    stats = calculate_work_statistics(
        3,
        ["ala", "ma", "kota", "ala"]
    )

    print(stats)

    assert stats["num_lines"] == 3
    assert stats["num_words"] == 4
    assert stats["unique_num_words"] == 3

def test_compare_works():
    works = {
        Path("A.txt"): (1, ["ala", "ma"]),
        Path("B.txt"): (1, ["ala", "ma"]),
    }

    similarity = compare_works(works)

    assert similarity is not None