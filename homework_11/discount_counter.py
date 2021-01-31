class Order:
    def __init__(self, price, discount_func):
        self.price = price
        if not isinstance(discount_func(), (float, int)):
            raise TypeError(
                "Discount function returned wrong type of value," " need float or int"
            )
        self.discount_func = discount_func

    def final_price(self):
        return self.price - self.price * self.discount_func()


"""
Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy
"""
