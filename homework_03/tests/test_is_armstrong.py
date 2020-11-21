import pytest

from homework_03.is_armstrong import is_armstrong


@pytest.mark.parametrize(
    ["value", "expected_result"], [(9, True), (153, True), (154, False), (int(), True)]
)
def test_is_armstrong(value, expected_result):
    actual_result = is_armstrong(value)
    assert actual_result == expected_result


@pytest.mark.parametrize(["value"], [[9.0], ["nine"], [str()], [True], [False]])
def test_wrong_type_of_input(value):
    with pytest.raises(Exception, match="Value is not integer"):
        is_armstrong(value)
