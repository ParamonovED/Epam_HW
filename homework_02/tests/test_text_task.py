import pytest

from homework_02.text_task import get_longest_diverse_words, get_rarest_char


def test_get_longest_diverse_words_long_before_short():
    expected_result = [
        "longword",
        "shorter",
        "eight",
        "words",
        "eleven",
        "seven",
        "five",
        "then",
        "ten",
        "nine",
    ]
    assert get_longest_diverse_words("test01.txt") == expected_result


def test_get_longest_diverse_words_punctuation():
    expected_result = [
        "Punctuation",
        "punctuation",
        "second",
        "First",
        "some",
        "word",
        "end",
        "the",
        "and",
        "of",
    ]
    assert get_longest_diverse_words("test02.txt") == expected_result


def test_get_longest_diverse_words_empty_lines():
    expected_result = [
        "eight",
        "lines",
        "empty",
        "seven",
        "this",
        "like",
        "with",
        "file",
        "ten",
        "nine",
    ]
    assert get_longest_diverse_words("test04.txt") == expected_result


def test_get_rarest_char():
    expected_result = "fwmpykvg"
    assert get_rarest_char("test04.txt") == expected_result


def test_get_longest_diverse_words_less_than_10_words():
    with pytest.raises(Exception, match="Too small amount of words"):
        get_longest_diverse_words("test03.txt")
