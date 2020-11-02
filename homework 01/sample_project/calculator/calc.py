def check_power_of_2(a: int) -> bool:
    if not isinstance(a, int):
        raise TypeError("Value must be int")
    if a == 0:
        return False
    return not (bool(a & (a - 1)))
