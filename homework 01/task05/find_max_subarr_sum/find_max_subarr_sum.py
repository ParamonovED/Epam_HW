"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if k > len(nums):
        raise ValueError("'k' must be less than 'nums'")
    ans = 0
    for i in range(len(nums) - (k - 1)):
        tmp = 0
        for j in range(k):
            tmp += nums[i + j]
        if ans < tmp:
            ans = tmp
    return ans
