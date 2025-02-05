"""Module with doctest approach"""


def is_even(n: int) -> bool:
    """
    Checks if number is even.

    >>> is_even(2)
    True
    >>> is_even(3)
    False
    >>> is_even(0)
    True
    >>> is_even(-4)
    True
    >>> is_even(-3)
    False
    """
    return n % 2 == 0


def factorial(n: int) -> int:
    """
    Returns factorial.

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> factorial(3)
    6
    >>> factorial(7)
    5040
    """
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
