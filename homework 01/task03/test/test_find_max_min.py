from typing import Tuple

import pytest
from model.find_max_min import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        ("test1", (-3, 87)),
        ("test2", (5, 5)),
    ],
)
def test_find_maximum_and_minimum(file_name: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(file_name)

    assert actual_result == expected_result
