"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List


def tokenize(file_path: str):
    with open(file_path, "r", encoding="unicode-escape", errors="replace") as fi:
        buffer = ""
        symbols = (symbol for line in fi for symbol in line)
        for symbol in symbols:
            if symbol.isspace():
                if len(buffer) > 0:
                    yield "word", buffer
                    buffer = ""
                yield "space", symbol
                continue
            if not symbol.isspace() and not symbol.isalnum():
                if len(buffer) > 0:
                    yield "word", buffer
                    buffer = ""
                yield "punctuation", symbol
                continue
            buffer += symbol


def get_longest_diverse_words(file_path: str) -> List[str]:
    top_10 = [""]
    for symbol in tokenize(file_path):
        if symbol[0] == "word":
            for place in top_10:
                if len(set(symbol[1])) >= len(set(place)) and symbol[1] not in top_10:
                    if symbol[1] == place:
                        break
                    top_10.insert(top_10.index(place), symbol[1])
                    top_10 = top_10[:10]
                    break
    if len(top_10) < 10:
        raise Exception("Too small amount of words")
    return top_10


def get_rarest_char(file_path: str) -> str:
    ans = dict()
    for word in tokenize(file_path):
        for symbol in word[1]:
            if symbol in ans.keys():
                ans[symbol] += 1
            else:
                ans[symbol] = 1
    rarest = ""
    for k, v in ans.items():
        if v == min(ans.values()):
            rarest += k
    return rarest


def count_punctuation_chars(file_path: str) -> int:
    count = 0
    for symbol in tokenize(file_path):
        if symbol[0] == "punctuation":
            count += 1
    return count


def count_non_ascii_chars(file_path: str) -> int:
    count = 0
    for word in tokenize(file_path):
        for symbol in word[1]:
            if not symbol.isascii():
                count += 1
    return count


def get_most_common_non_ascii_char(file_path: str) -> str:
    ans = dict()
    for word in tokenize(file_path):
        for symbol in word[1]:
            if not symbol.isascii():
                if symbol in ans.keys():
                    ans[symbol] += 1
                else:
                    ans[symbol] = 1
    ans = dict(zip(ans.values(), ans.keys()))
    return f"{ans[max(ans)]}"


# print(get_longest_diverse_words("test02.txt"))  # 8277 # 5476
