from homework_07.hw3 import tic_tac_toe_checker


def test_x_line_wins():
    assert (
        tic_tac_toe_checker([["-", "-", "o"], ["-", "x", "o"], ["x", "x", "x"]])
        == "x wins!"
    )


def test_x_diag_wins():
    assert (
        tic_tac_toe_checker([["x", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]])
        == "x wins!"
    )


def test_draw():
    assert (
        tic_tac_toe_checker([["x", "o", "o"], ["o", "x", "x"], ["x", "o", "o"]])
        == "draw!"
    )


def test_unfinished():
    assert (
        tic_tac_toe_checker([["x", "o", "o"], ["o", "-", "x"], ["x", "o", "o"]])
        == "unfinished"
    )
