from unittest.mock import Mock, call

from homework_02.cacher import cache


def test_cacher():
    mock = Mock()

    def f(a):
        ans = a ** 2
        return ans

    f_mock = mock(f)
    cached = cache(f_mock)

    cached(1)
    cached(1)
    cached(2)
    cached(3)
    cached(2)
    cached(2)

    actual_result = mock.mock_calls
    expected_result = [call(f), call()(1), call()(2), call()(3)]
    assert expected_result == actual_result


def test_cacher_values():
    @cache
    def f(c):
        ans = c ** 2
        return ans

    a = f(3)
    b = f(3)
    assert a == b
