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
    if tree != element and isinstance(tree, (list, set, tuple)):
        counter += find_occurrences(dict(enumerate(tree)), element)
    if isinstance(tree, dict):
        for branch, value in tree.items():
            counter += find_occurrences(value, element)
    counter += element == tree
    return counter
