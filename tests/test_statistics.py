from analyzer.statistics import calculate_statistics

def test_calculate_statistics():
    stats = calculate_statistics(
        3,
        ["a", "b", "a"]
    )

    assert stats["num_lines"] == 3
    assert stats["num_words"] == 3