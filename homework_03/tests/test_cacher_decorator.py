from unittest.mock import Mock, call

import pytest

from homework_03.cacher_decorator import cache


def test_cacher_decorator():
    mock = Mock()

    def f(*args, **kwargs):
        return args, kwargs

    mock_f = mock(f)
    cached = cache(2)(mock_f)

    cached(2, 3, 4, five=5, six=6)
    cached(2, 3, 4, five=5, six=6)
    for i in range(5):
        cached(left_hand="snickers", right_hand="mars")
    actual_result = mock.mock_calls
    expected_result = [
        call(f),
        call()(2, 3, 4, five=5, six=6),
        call()(left_hand="snickers", right_hand="mars"),
        call()(left_hand="snickers", right_hand="mars"),
    ]
    assert actual_result == expected_result


def test_cacher_decorator_zero():
    mock = Mock()

    def f(*args, **kwargs):
        return args, kwargs

    mock_f = mock(f)
    cached = cache(0)(mock_f)

    cached(1)
    cached(2)
    cached(2)

    actual_result = mock.mock_calls
    expected_result = [call(f), call()(1), call()(2), call()(2)]
    assert expected_result == actual_result


@pytest.mark.parametrize(
    ["first", "second"],
    [
        (1, 1),
        [[], []],
        ["str", "str"],
        [True, True],
    ],
)
def test_cacher_decorator_check_inputs(first, second):
    @cache(2)
    def f(*args, **kwargs):
        return args, kwargs

    first = f(first)
    second = f(second)

    assert first is second


@pytest.mark.parametrize(["first", "second"], [(1, 1.0), [True, 1]])
def test_cacher_decorator_check_different_inputs(first, second):
    @cache(2)
    def f(*args, **kwargs):
        return args, kwargs

    first = f(first)
    second = f(second)

    assert first is not second
