"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    top_10 = []
    with open(file_path) as fi:
        file = fi.readlines()
        temp_top = file[0][0]
        for i in range(10):
            for line in file:
                line = line.strip().split(" ")
                for word in line:
                    word = word.strip().encode().decode("unicode-escape")
                    if len(word) > 0:
                        if not word[-1].isalnum():
                            word = word[:-1]
                    if len(set(word)) >= len(set(temp_top)) and word not in top_10:
                        temp_top = word
            if id(temp_top) != id(file[0][0]):
                top_10.append(temp_top)
                temp_top = file[0][0]
    if len(top_10) < 10:
        raise Exception("Too small amount of words")
    return top_10[:10]


def get_rarest_char(file_path: str) -> str:
    ans = dict()
    with open(file_path) as fi:
        for line in fi:
            for symbol in line:
                tmp = line.count(symbol)
                if symbol in ans.keys():
                    ans[symbol] += tmp
                else:
                    ans[symbol] = tmp
    ans = dict(zip(ans.values(), ans.keys()))
    return f"{ans[min(ans)]}"


def count_punctuation_chars(file_path: str) -> int:
    count = 0
    with open(file_path) as fi:
        gen = (symbol for line in fi for symbol in line)
        for i in gen:
            if not i.isalnum() and not i.isspace():
                count += 1
    return count


def count_non_ascii_chars(file_path: str) -> int:
    count = 0
    with open(file_path) as fi:
        symbols = (symbol for line in fi for symbol in line)
        for symbol in symbols:
            if symbol.encode().decode("unicode-escape", errors="ignore") != symbol:
                count += 1
            print(symbol.encode().decode("unicode-escape", errors="ignore"), symbol)
    return count


def get_most_common_non_ascii_char(file_path: str) -> str:
    ans = dict()
    with open(file_path) as fi:
        for line in fi:
            for symbol in line:
                if not symbol.isascii():
                    tmp = line.count(symbol)
                    if symbol in ans.keys():
                        ans[symbol] += tmp
                    else:
                        ans[symbol] = tmp
    ans = dict(zip(ans.values(), ans.keys()))
    return f"{ans[min(ans)]}"


# print(get_longest_diverse_words('test3.txt'))
