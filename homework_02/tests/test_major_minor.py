from typing import List

import pytest

from homework_02.major_minor import major_and_minor_elem


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([3, 2, 3], (3, 2)),
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
        (["a", "s", "a", "d", "c", "d", "a", "a"], ("a", "c")),
        ([1, 2, 4, 4], (4, 2)),
        ([0, 1, 2, 3, 4, 4], (None, 3)),
    ],
)
def test_major_and_minor_elem(value: List, expected_result: tuple):
    actual_result = major_and_minor_elem(value)
    assert actual_result == expected_result


def test_major_and_minor_typeerror():
    with pytest.raises(TypeError, match="Input must be List"):
        major_and_minor_elem("str")


def test_major_and_minor_valueerror():
    with pytest.raises(Exception, match="Need more than 2 values"):
        major_and_minor_elem([])


def test_major_and_minor_elem_raises():
    with pytest.raises(Exception, match="Need more than 2 values"):
        major_and_minor_elem([1, 1])
