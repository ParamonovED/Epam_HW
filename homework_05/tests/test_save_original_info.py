import functools

import pytest

from homework_05.save_original_info import custom_sum

# def save_func(original_func):

#  print_result(func):


def test_doc_printing():
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"


def test_name_printing():
    assert custom_sum.__name__ == "custom_sum"


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [((1, 2, 3, 4), 10), (([1, 2, 3], [4, 5]), [1, 2, 3, 4, 5]), (("a", "bc"), "abc")],
)
def test_result_printing(value, expected_result):
    assert custom_sum(*value) == expected_result


"""(capsys):
    my_precious_logger("cheburek")
    captured = capsys.readouterr()
    assert captured.out == "cheburek"
    assert captured.err == """ ""

"""if __name__ == "__main__":
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)

    print(custom_sum.__doc__)
    print(custom_sum.__name__)
    without_print = custom_sum.__original_func
    # the result returns without printing
    without_print(1, 2, 3, 4)"""
