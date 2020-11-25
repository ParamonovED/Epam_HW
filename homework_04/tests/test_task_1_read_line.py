import os

import pytest

from homework_04.task_1_read_file import read_magic_number


@pytest.fixture()
def create_file(tmpdir_factory):
    filename = tmpdir_factory.mktemp("data").join("tmp_file.txt")
    yield filename

    try:
        os.remove(filename)
    except IOError:
        pass


@pytest.mark.parametrize("value", [1, 2])
def test_positive_case(value, create_file):
    file_name = create_file
    with open(file_name, "w") as file:
        file.write(str(value))
    actual_result = read_magic_number(file_name)
    assert actual_result == True


@pytest.mark.parametrize("value", [0, 3])
def test_negative_case(value, create_file):
    with open(create_file, "w") as file:
        file.write(str(value))
    actual_result = read_magic_number(create_file)
    assert actual_result == False


def test_empty_file(create_file):
    with open(create_file, "w") as file:
        file.write(str(""))
    with pytest.raises(ValueError, match="Empty file"):
        read_magic_number(create_file)
