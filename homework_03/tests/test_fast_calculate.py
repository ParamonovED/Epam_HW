import time

from homework_03.fast_calculate import fast_calculate


def test_fast_calculate():
    time_start = time.time()
    fast_calculate(50, 500)
    time_finish = time.time()
    time_executing = time_finish - time_start
    assert time_executing <= 60
