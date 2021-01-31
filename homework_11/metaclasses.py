"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
"""


class SimplifiedEnum(type):
    _instances = {}

    def __new__(mcs, name, bases, dct):
        if name not in mcs._instances:
            tmp_dct = {key: key for key in dct[f"_{name}__keys"]}
            # code above looks quite bad, is it possible to make more beautiful?
            mcs._instances[name] = super().__new__(mcs, name, bases, tmp_dct)
        else:
            print(f"Class '{name}' already exists")
        return mcs._instances[name]
