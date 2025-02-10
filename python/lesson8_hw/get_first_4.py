"""Module with funciton get_first"""

from typing import List, TypeVar, Optional

T = TypeVar("T")


def get_first(inp_list: List[T]) -> Optional[T]:
    """Function get first"""
    return inp_list[0] if inp_list else None


if __name__ == "__main__":
    print(get_first([1, 2, 3]))
    print(get_first(["a", "b", "c"]))
    print(get_first([]))
