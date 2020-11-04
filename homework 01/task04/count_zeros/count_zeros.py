"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    count = 0
    for i in a:
        for j in b:
            for k in c:
                for m in d:  # because "l" is ambigious variable
                    if i + j + k + m == 0:
                        count += 1
    return count


# print(type(check_sum_of_four([1, 2, 3, 4], [2, 3, -3, 2], [-2, -4, -2, -4], [1, -1, 3, -2])))
