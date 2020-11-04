from typing import List

import pytest
from find_max_subarr_sum.find_max_subarr_sum import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["nums", "k", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([-1, -2, -3, 1], 3, 1),
        ([-1, -2, -3, -4], 2, -1),
    ],
)
def test_find_maximal_subarray_sum(nums: List[int], k: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(nums, k)
    assert actual_result == expected_result


def test_find_maximal_subarray_sum_raises():
    with pytest.raises(ValueError):
        actual_result = find_maximal_subarray_sum([1, 3, 6, 7], 5)
        assert actual_result == ValueError
