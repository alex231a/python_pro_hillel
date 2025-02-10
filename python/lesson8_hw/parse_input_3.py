"""Module with function parse_input"""
from typing import Union


def parse_input(val: Union[int, str]) -> Union[int, None]:
    """Function parse_input"""
    if isinstance(val, str):
        try:
            return int(val)
        except ValueError:
            return None
    return int(val)


if __name__ == "__main__":
    print(parse_input(42))
    print(parse_input("100"))
    print(parse_input("hello"))
