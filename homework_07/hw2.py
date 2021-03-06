"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""


def backspace_compare(first: str, second: str):
    return backspace_tapping(reversed(first)) == backspace_tapping(reversed(second))


def backspace_tapping(word):
    counter = 0
    answer = ""
    for symbol in word:
        if symbol == "#":
            counter += 1
        if symbol != "#" and counter == 0:
            answer += symbol
        if symbol != "#" and counter != 0:
            counter -= 1
    return answer
