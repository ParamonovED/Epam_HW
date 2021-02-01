import pytest

from homework_08.class_wrapper import KeyValueStorage


@pytest.fixture
def rollback_file():
    yield
    with open("task1.txt", "w") as fi:
        fi.writelines("first_name=kek\nlast_name=top\nsong_name=shadilay\npower=9001\n")


@pytest.fixture
def create_object():
    yield KeyValueStorage("task1.txt")


def test_creting_an_object():
    x = KeyValueStorage("task1.txt")
    assert isinstance(x, KeyValueStorage)


def test_check__dict__(create_object, rollback_file):
    create_object = KeyValueStorage("task1.txt")

    assert create_object.__dict__ == {
        "file_name": "task1.txt",
        "last_name": "top",
        "first_name": "kek",
        "power": 9001,
        "song_name": "shadilay",
    }


def test_check_int(create_object):
    assert isinstance(create_object.power, int)


def test_check_values(create_object):
    assert create_object.first_name == "kek"


def test_set_built_in_attribute(create_object):
    create_object.__new__ = "Hello"
    assert create_object.__new__ != "Hello"


def test_setted_attribute_writed_in_file(create_object, rollback_file):
    """We have only no "Hello" in that file"""
    create_object.hi = "Hello"
    with open("task1.txt") as fi:
        assert sum(line.count("Hello") for line in fi.readlines()) == 1


def test_rewriting_key(create_object, rollback_file):
    create_object.hi = "Hello"
    create_object.hi = "Olleh"
    with open("task1.txt") as fi:
        assert sum(line.count("Hello") for line in fi.readlines()) == 1
    assert create_object.__dict__["hi"] == "Hello"


def test_raise_wrong_key_exception(create_object):
    with pytest.raises(ValueError):
        create_object.__setattr__(5, 455)
