"""Module with class Processor"""
from typing import List, TypeVar, Callable

T = TypeVar("T")


class Processor:
    """Class processor"""

    def __init__(self, data: List[T]) -> None:
        """init method"""
        self.data = data

    def apply(self, function: Callable[[T], T]) -> List[T]:
        """Apply method"""
        return [function(item) for item in self.data]


if __name__ == "__main__":
    def double(value: int) -> int:
        """Function double"""
        return value * 2


    def to_upper(value: str) -> str:
        """Function to_upper"""
        return value.upper()


    p1 = Processor([1, 2, 3])
    print(p1.apply(double))

    p2 = Processor(["hello", "world"])
    print(p2.apply(to_upper))
