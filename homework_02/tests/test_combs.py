from typing import Any, List

import pytest

from homework_02.combs import combinations


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (([1, 2], [3, 4]), [[1, 3], [1, 4], [2, 3], [2, 4]]),
        ((["a", "b"], ["y", "z"]), [["a", "y"], ["a", "z"], ["b", "y"], ["b", "z"]]),
    ],
)
def test_combinations(value: List[Any], expected_result: List[List]):
    actual_result = combinations(*value)
    assert actual_result == expected_result


def test_combinations_raise():
    with pytest.raises(Exception, match="All lists mustn't be empty"):
        combinations([], [3, 4])
