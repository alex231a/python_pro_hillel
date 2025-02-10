"""Module with apply_operation function"""

from typing import Union, Callable


def apply_operation(x_val: Union[int, float], operation: Callable[
    [Union[int, float]], Union[int, float]]) -> Union[int, float]:
    """function apply_operation"""
    return operation(x_val)


def square(x_val: Union[int, float]) -> Union[int, float]:
    """function square"""
    return x_val * x_val


def double(x_val: Union[int, float]) -> Union[int, float]:
    """function double"""
    return x_val * 2


if __name__ == "__main__":
    print(apply_operation(5, square))  # 25
    print(apply_operation(5, double))  # 10
