import pytest

from homework_03.filter_debug import make_filter


def test_return_value_by_key():
    sample_data = [
        {"name": "Bill", "last_name": "Gilbert"},
        {"type": "bird", "name": "polly"},
    ]
    actual_result = make_filter(name="Bill").apply(sample_data)
    assert actual_result == [{"name": "Bill", "last_name": "Gilbert"}]


def test_wrong_key():
    sample_data = [
        {"name": "Bill", "last_name": "Gilbert"},
        {"type": "bird", "name": "polly"},
    ]

    with pytest.raises(KeyError, match="Can't find key 'naim'"):
        make_filter(naim="Bill").apply(sample_data)


def test_wrong_value():
    sample_data = [
        {"name": "Bill", "last_name": "Gilbert"},
        {"type": "bird", "name": "polly"},
    ]
    actual_result = make_filter(name="Bob").apply(sample_data)
    assert actual_result == []


def test_wrong_some_of_values():
    sample_data = [
        {"name": "Bill", "last_name": "Gilbert"},
        {"type": "bird", "name": "polly"},
    ]
    actual_result = make_filter(name="polly", type="dog").apply(sample_data)
    assert actual_result == []


def test_empty_value():
    """
    Did i need to change result?
    I think if we have no filters we accept all items in data
    """
    sample_data = [
        {"name": "Bill", "last_name": "Gilbert"},
        {"type": "bird", "name": "polly"},
    ]
    actual_result = make_filter().apply(sample_data)
    assert actual_result == [
        {"name": "Bill", "last_name": "Gilbert"},
        {"type": "bird", "name": "polly"},
    ]


def test_for_non_unique_answer():
    sample_data = [
        {"name": "Bill", "last_name": "Gilbert"},
        {"name": "Bill", "type": "dog"},
    ]
    actual_result = make_filter(name="Bill").apply(sample_data)
    assert actual_result == [
        {"name": "Bill", "last_name": "Gilbert"},
        {"name": "Bill", "type": "dog"},
    ]


def test_for_two_same_items():
    sample_data = [
        {"name": "Bill", "last_name": "Gilbert"},
        {"name": "Bill", "last_name": "Gilbert"},
    ]
    actual_result = make_filter(name="Bill").apply(sample_data)
    assert actual_result == [
        {"name": "Bill", "last_name": "Gilbert"},
        {"name": "Bill", "last_name": "Gilbert"},
    ]
