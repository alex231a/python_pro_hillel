def factorial(n: int):
    """Function that finds factorial"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def gcd(a: int, b: int):
    """Function to calculate the greatest common divisor """
    while b:
        a, b = b, a % b
    return a
