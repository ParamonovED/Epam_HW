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
        (([1, 2, "ha-ha", 4, 5, 6, 7, 8, 9, 0], 5), [1, 2, "ha-ha", 4]),
        (([1, 2, "ha-ha", 4, 5, 6, 7, 8, 9, 0], "ha-ha", 5), ["ha-ha", 4]),
        (([1, 2, "ha-ha", 4, 5, 6, 7, 8, 9, 0], 8, 2, -2), [8, 6, 4]),
        (([set, list, tuple(), tuple, 3, str(), str], tuple), [set, list, tuple()]),
    ],
)
def test_custom_range(value: Sequence, expected_result: Sequence):
    actual_result = custom_range(*value)
    assert actual_result == expected_result


@pytest.mark.parametrize("value", ["abcc", [1, True], [0, False]])
def test_custom_range_assert_non_unique(value):
    with pytest.raises(Exception, match="Input consist non-unique values"):
        custom_range(value, 5)


def test_custom_range_assert_no_elements():
    with pytest.raises(Exception, match="Input have no elements"):
        custom_range([], 0)
