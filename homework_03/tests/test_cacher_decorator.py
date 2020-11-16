from unittest.mock import Mock, call

import pytest

from homework_03.cacher_decorator import cache


def test_cacher_decorator():
    mock = Mock()
    f = mock()
    dec = cache(f, 2)
    dec(1)
    dec(1)
    dec(2)
    dec(2)
    dec(2)
    dec(2)

    mock.assert_has_calls(mock.mock_calls)
    actual_result = mock.mock_calls
    expected_result = [call(), call()(1), call()(2), call()(2)]
    assert expected_result == actual_result
