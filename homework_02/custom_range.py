"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']


This function accept only values, that have different hash or id.
"""


def custom_range(ranged, start, stop=None, step=1):
    if len(ranged) == 0:
        raise Exception("Input have no elements")
    if len(set(ranged)) != len(ranged):
        raise Exception("Input consist non-unique values")
    if stop is None:
        stop = start
        start = ranged[0]
    return [s for s in ranged[ranged.index(start) : ranged.index(stop) : step]]
