"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    for i in range(3):
        if comparer(*board[i]) or comparer(board[0][i], board[1][i], board[2][i]):
            return f"{str(board[i][i])} wins!"

    if comparer(*[board[i][i] for i in range(3)]) or comparer(
        *[board[2 - i][i] for i in range(3)]
    ):
        return f"{str(board[1][1])} wins!"

    if sum(board[i].count("-") for i in range(3)) == 0:
        return "draw!"
    else:
        return "unfinished"


def comparer(*elements):
    ans = len(set(elements)) == 1
    return ans
