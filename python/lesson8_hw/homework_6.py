"""Module with homeworks"""
from typing import List, Tuple, Union, Optional, TypeVar, Callable


def calculate_discount(price: float, discount: float) -> float:
    """Function counts discount"""
    if discount >= 100:
        return 0.0
    return price - ((price * discount) / 100)


def filter_adults(people_list: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """Function filter_adults returns only adults"""
    return [tup for tup in people_list if tup[1] >= 18]


def parse_input(val: Union[int, str]) -> Union[int, None]:
    """Function parse_input"""
    if isinstance(val, str):
        try:
            return int(val)
        except ValueError:
            return None
    return int(val)


T = TypeVar("T")


def get_first(inp_list: List[T]) -> Optional[T]:
    """Function get first"""
    return inp_list[0] if inp_list else None


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
