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

    return (i for i in merge_sort(big_massive))  # maybe sorted(big_massive)


def merge_sort(data_list: List) -> List:
    if len(data_list) < 2:
        return data_list

    middle = len(data_list) // 2
    half_1 = data_list[:middle]
    half_2 = data_list[middle:]

    range1 = merge_sort(half_1)
    range2 = merge_sort(half_2)

    index_1 = index_2 = index_result = 0
    result = [0] * len(data_list)

    while index_1 < len(range1) and index_2 < len(range2):
        if range1[index_1] <= range2[index_2]:
            result[index_result] = range1[index_1]
            index_1 += 1
            index_result += 1
        else:
            result[index_result] = range2[index_2]
            index_2 += 1
            index_result += 1

    while index_1 < len(range1):
        result[index_result] = range1[index_1]
        index_1 += 1
        index_result += 1

    while index_2 < len(range2):
        result[index_result] = range2[index_2]
        index_2 += 1
        index_result += 1

    return result
