import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def fast_calculate(processes, number_of_calculates):
    with Pool(processes) as p:
        res = sum(p.map(slow_calculate, range(number_of_calculates)))
    return res


if __name__ == "__main__":
    print(fast_calculate(50, 100))
