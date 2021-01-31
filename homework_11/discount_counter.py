"""
You are given the following code:
"""


class Order:
    def __init__(self, price, discount_func):
        self.price = price
        self.discount_func = discount_func

    def final_price(self):
        return self.price - self.price * self.discount_func()


"""
Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:
"""


def morning_discount():
    return 0.5


def elder_discount():
    return 0.9


order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50

order_2 = Order(100, elder_discount)
assert order_2.final_price() == 10
