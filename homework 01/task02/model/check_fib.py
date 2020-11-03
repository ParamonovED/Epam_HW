"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence  # 'ABCMeta' object is not subscriptable


def check_fibonacci(data: Sequence[int]) -> bool:
    ans = False
    tmp1 = 0
    tmp2 = 1
    tmp3 = 1
    while tmp1 < data[0]:
        tmp1, tmp2, tmp3 = tmp2, tmp3, tmp2 + tmp3
    if tmp1 == data[0]:
        for i in range(len(data)):
            if data[i] == tmp1:
                ans = True
            else:
                ans = False
                break
            tmp1, tmp2, tmp3 = tmp2, tmp3, tmp2 + tmp3
    return ans
