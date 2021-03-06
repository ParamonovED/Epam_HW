from typing import Tuple

import pytest

from homework_01.find_max_min import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        ("test1.txt", (-3, 87)),
        ("test2.txt", (5, 5)),
    ],
)
def test_find_max_min(file_name: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(file_name)

    assert actual_result == expected_result
