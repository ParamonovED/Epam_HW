from homework_07.hw2 import backspace_compare


def test_one_backspace_in_the_middle():
    assert backspace_compare("fa#c", "fs#c")


def test_backspace_in_the_start():
    assert backspace_compare("#ac", "ac")


def test_double_backspace():
    assert backspace_compare("abc##d", "ad")


def test_different_words():
    assert not backspace_compare("a#c", "a#b")
