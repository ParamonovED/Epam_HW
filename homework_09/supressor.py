"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with supressor_class(IndexError):
...    [][2]

>>> with supressor_gen(IndexError):
...    [][2]
"""
from contextlib import contextmanager


class supressor_class:
    def __init__(self, type_exception):
        self.type_exception = type_exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == self.type_exception:
            return True


@contextmanager
def supressor_gen(type_exception):
    try:
        yield
    except type_exception:
        return True
