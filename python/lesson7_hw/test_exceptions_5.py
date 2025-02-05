"""Tests for checking function divide"""

import pytest


def divide(a: int, b: int) -> float:
    """Function divides two numbers and returns result"""
    if b == 0:
        raise ZeroDivisionError
    return a / b


@pytest.mark.parametrize("a, b, expected",
                         [(3, 1, 3.0), (5, 3, 1.67), (10, 2, 5.0),
                          (5, 15, 0.33)])
def test_divide(a, b, expected):
    """Parametrize tests for divide function"""
    assert round(divide(a, b),
                 2) == expected, (f"expected {expected} got "
                                  f"{round(divide(6, 2), 2)}")


def test_divide_zero():
    """Test that checks division by zero"""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


if __name__ == "__main__":
    pytest.main()
