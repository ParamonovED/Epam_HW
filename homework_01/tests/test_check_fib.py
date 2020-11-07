from typing import Sequence

import pytest

from homework_01.check_fib import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([1, 1, 2, 3], True),
        ([13, 21, 34], True),
        ([1, 3, 5], False),
        ([4], False),
        ([3], True),
        ([3, 3, 6], False),
        ([], True),
    ],
)
def test_check_fib(value: Sequence[int], expected_result: bool):
    actual_result = check_fibonacci(value)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("zero", TypeError),
    ],
)
def test_check_fib_raises(value, expected_result):
    with pytest.raises(expected_result):
        test_check_fib(value)
