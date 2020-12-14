import pytest

from homework_08.data_base_class import TableData


@pytest.fixture
def create_presidents():
    yield TableData("example.sqlite", "presidents")


def test_creating_class():
    presidents = TableData("example.sqlite", "presidents")
    assert isinstance(presidents, TableData)


def test_check_len(create_presidents):
    assert len(create_presidents) == 3


def test_check_printing_row_by_keyword(
    create_presidents,
):  # I decided keyword will be name of president
    presidents = create_presidents
    assert presidents["Yeltsin"] == [("Yeltsin", 999, "Russia")]


def test_(create_presidents):
    assert "Trump" in create_presidents


def test_returning_coulumn(create_presidents):
    answer = []
    for president in create_presidents:
        answer.append(president["country"])  # of course, if u know name of coulumn
    assert answer == ["Russia", "US", "Kekistan"]


def test_raise_if_wrong_key(create_presidents):
    with pytest.raises(KeyError, match="key 'wrong_key' not found"):
        answer = []
        for president in create_presidents:
            answer.append(president["wrong_key"])
