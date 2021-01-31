import pytest

from homework_11.metaclasses import SimplifiedEnum


def test_sample():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")

    assert ColorsEnum.RED == "RED"
    assert SizesEnum.XL == "XL"


def test_all_created_instances_save_in__instances():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")

    assert "ColorsEnum" in SimplifiedEnum._instances.keys()


def test_try_rewrite_instance():
    class TurnEnum(metaclass=SimplifiedEnum):
        __keys = ("RIGHT", "LEFT")

    class TurnEnum(metaclass=SimplifiedEnum):
        __keys = ("RIGHT", "LEFT", "UP", "DOWN")

    with pytest.raises(AttributeError):
        TurnEnum.UP


def test_print_warning_when_instance_is_rewrited(capsys):
    class OneEnum(metaclass=SimplifiedEnum):
        __keys = "ONE"

    class OneEnum(metaclass=SimplifiedEnum):
        __keys = "ONE"

    captured = capsys.readouterr()
    assert captured.out == "Class 'OneEnum' already exists\n"
