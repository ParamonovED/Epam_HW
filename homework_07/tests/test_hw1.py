import pytest

from homework_07.hw1 import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def test_example():
    assert find_occurrences(example_tree, "RED") == 6


boolean_tree = {"True": True, "zero": 0, "one": 1, "False": False}


@pytest.mark.parametrize("value", [True, False, 0, 1])
def test_booleans(value):
    assert find_occurrences(boolean_tree, value) == 2


tuple_tree = {
    "target_tuple": (1, "one"),
    "one more dict": {"one_more_tuple": (1, "one"), "another_tuple": (1, 2)},
}


def test_tuples():
    assert find_occurrences(tuple_tree, (1, "one")) == 2


def test_inside_tuples():
    assert find_occurrences(tuple_tree, "one") == 2


list_tree = {
    "target_list": ["RED", "BLUE"],
    "one more_list": ["another_value", ["RED", "BLUE"]],
}


def test_lists():
    assert find_occurrences(list_tree, ["RED", "BLUE"]) == 2


set_tree = {
    "simple_set": set("RED"),
    "one_more_set": {"set": set("RED"), "notset": "RED"},
}


def test_in_set():
    assert find_occurrences(set_tree, "R") == 2


def test_set():
    assert find_occurrences(set_tree, set("DER")) == 2


int_tree = {"one": 1, "list": [0, 1, {"one_nore": 1}, 1], "not_one_more": "1"}


def test_int():
    assert find_occurrences(int_tree, 1) == 4
