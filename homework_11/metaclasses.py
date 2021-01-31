"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
"""
# from enum import Enum


# class ColorsEnum(Enum):
#     RED = "RED"
#     BLUE = "BLUE"
#     ORANGE = "ORANGE"
#     BLACK = "BLACK"
#
#
# class SizesEnum(Enum):
#     XL = "XL"
#     L = "L"
#     M = "M"
#     S = "S"
#     XS = "XS"


class SimplifiedEnum(type):
    _instances = {}

    def __new__(mcs, name, bases, dct):
        if name not in mcs._instances:
            tmp = {key: key for key in dct[f"_{name}__keys"]}
            # code above looks quite bad, is it possible to make more beautiful?
            mcs._instances[mcs] = super().__new__(mcs, name, bases, tmp)
        return mcs._instances[mcs]


class ColorsEnum(metaclass=SimplifiedEnum):  # Enum?
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
