"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import List, Union, Iterator


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    big_massive = []
    for file in file_list:
        with open(file, "r") as fi:
            for line in fi:
                big_massive.append(int(line.strip()))

    return (i for i in sorted(big_massive))
