import pytest

from homework_11.discount_counter import Order


def test_sample():
    def morning_discount():
        return 0.5

    def elder_discount():
        return 0.9

    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 50

    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10


def test_zero_discount():
    def zero_discount():
        return 0

    order = Order(100, zero_discount)
    assert order.final_price() == 100


def test_one_hundred_discount():
    def one_hundred_discount():
        return 1

    order = Order(100, one_hundred_discount)
    assert order.final_price() == 0


def test_discount_with_zero_price():
    def zero_discount():
        return 0.5

    order = Order(0, zero_discount)
    assert order.final_price() == 0


def test_negative_discount():
    def negative_discount():
        return -0.5

    order = Order(100, negative_discount)
    assert order.final_price() == 150


def test_bad_discount():
    def bad_discount():
        return ""

    with pytest.raises(TypeError):
        order = Order(100, bad_discount)


def test_so_big_discount():
    def so_big_discount():
        return 2

    order = Order(100, so_big_discount)
    assert order.final_price() == -100
