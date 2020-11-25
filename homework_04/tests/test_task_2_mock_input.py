"""
Warning! This module has dependence on internet connection. For Independed testing turn off the first test!
"""
import urllib.request
from unittest.mock import Mock
from urllib.error import HTTPError

import pytest

from homework_04.task_2_mock_input import count_dots_on_i


def test_without_mock():
    actual_result = count_dots_on_i("https://example.com/")
    assert actual_result == 59


def test_positive_with_mock(monkeypatch):
    mock = Mock
    fake_page = mock(
        return_value=[b"<html><head>head</head><text>simple iximple</text></html>"]
    )
    monkeypatch.setattr(urllib.request, "urlopen", value=fake_page)

    actual_result = count_dots_on_i("https://example.com/")
    assert actual_result == 3


def test_negative_bad_connection(monkeypatch):
    url = "https://example.com/"
    mock = Mock
    response = mock(side_effect=HTTPError(404, "NF", "", "", ""))
    monkeypatch.setattr(urllib.request, "urlopen", value=response)
    with pytest.raises(Exception, match=f"Unreachable {url}"):
        count_dots_on_i(url)
