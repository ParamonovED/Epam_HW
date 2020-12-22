import pytest

from homework_09.supressor import supressor_class, supressor_gen


def test_sample():
    with supressor_class(IndexError):
        [][2]
    with supressor_gen(IndexError):
        [][2]


def test_other_error():
    with pytest.raises(ZeroDivisionError):
        with supressor_class(IndexError):
            5 / 0
        with supressor_gen(IndexError):
            5 / 0


def test_super_error():
    with pytest.raises(ZeroDivisionError):
        with supressor_class(Exception):
            5 / 0
        with supressor_gen(Exception):
            5 / 0


def test_double_error():
    with supressor_class(IndexError):
        [][2]
        [][3]
    with supressor_gen(IndexError):
        [][2]
        [][3]
