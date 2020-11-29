"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...


Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    Here main fizzbuzz function, but it won't work itself!
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']

    >>> fizzbuzz(15)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']

    >>> fizzbuzz(0)
    []

    """
    check_input(n)
    return [calculate_fizzbuzz(n) for n in range(1, n + 1)]


def calculate_fizzbuzz(n):
    """
    Here we calculate numbers. We can make some changes easily by this way

    >>> calculate_fizzbuzz(0)
    '0'

    >>> calculate_fizzbuzz(1)
    '1'

    >>> calculate_fizzbuzz(3)
    'fizz'

    >>> calculate_fizzbuzz(5)
    'buzz'

    >>> calculate_fizzbuzz(15)
    'fizzbuzz'
    """
    dividers = {15: "fizzbuzz", 3: "fizz", 5: "buzz"}
    for k, v in dividers.items():
        if n % int(k) == 0 and n > 0:
            return v
    return str(n)


def check_input(n):
    """
    That function checks is input is correct or not, we can't get get negative amount of values

    >>> fizzbuzz(-1)
    Traceback (most recent call last):
    ...
    ValueError: Input is not positive!

    """
    if n < 0:
        raise ValueError("Input is not positive!")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
