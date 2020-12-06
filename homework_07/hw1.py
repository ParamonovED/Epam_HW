"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    counter = 0
    for branch, value in tree.items():
        if isinstance(value, dict):
            counter += find_occurrences(value, element)
        if value == element:
            counter += 1
        if isinstance(value, (list, tuple, set)):
            counter += find_occurence(value, element)
    return counter


def find_occurence(tree: Any, element: Any):
    counter = 0
    for branch in tree:
        if isinstance(branch, dict):
            counter += find_occurrences(branch, element)
        if branch == element:
            counter += 1
    return counter
