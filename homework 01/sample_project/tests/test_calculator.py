import pytest
from calculator.calc import check_power_of_2


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [(65536, True), (12, False), (-65536, False), (0, False)],
)
def test_power_of_2(value: int, expected_result: bool):
    actual_result = check_power_of_2(value)
    assert actual_result == expected_result


def test_power_of_2_raises():
    with pytest.raises(TypeError):
        actual_result = test_power_of_2("eight")
        assert actual_result == TypeError
