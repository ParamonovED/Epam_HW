from typing import Sequence

import pytest
from model.check_fib import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([1, 1, 2, 3], True),
        ([13, 21, 34], True),
        ([1, 3, 5], False),
        ([4], False),
        ([3], True),
        ([3, 3, 6], False),
    ],
)
def test_find_maximum_and_minimum(value: Sequence[int], expected_result: bool):
    actual_result = check_fibonacci(value)

    assert actual_result == expected_result
