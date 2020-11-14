import string
from typing import Sequence

import pytest

from homework_02.custom_range import custom_range


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ((string.ascii_lowercase, "g"), ["a", "b", "c", "d", "e", "f"]),
        ((string.ascii_lowercase, "d", "h"), ["d", "e", "f", "g"]),
        ((string.ascii_lowercase, "p", "g", -2), ["p", "n", "l", "j", "h"]),
    ],
)
def test_custom_range(value: Sequence, expected_result: Sequence):
    actual_result = custom_range(*value)
    assert actual_result == expected_result


def test_custom_range_assert():
    with pytest.raises(Exception, match="Input consist non-unique values"):
        custom_range("abcdeeeefghjklmnop", "g")
