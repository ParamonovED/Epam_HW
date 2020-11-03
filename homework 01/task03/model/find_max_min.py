"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from math import inf
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name + ".txt") as fi:
        maxline = -inf
        minline = inf
        for line in fi:
            m = line.strip().split(",")
            m_ints = [int(i) for i in m]
            if maxline < max(m_ints):
                maxline = max(m_ints)
            if minline > min(m_ints):
                minline = min(m_ints)

            # maxline, minline = max(m_ints), min(m_ints)

        return minline, maxline
