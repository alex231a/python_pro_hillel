"""Module with function filter_adults"""
from typing import List, Tuple


def filter_adults(people_list: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """Function filter_adults returns only adults"""
    return [tup for tup in people_list if tup[1] >= 18]


if __name__ == "__main__":
    people = [("Андрій", 25), ("Олег", 16), ("Марія", 19), ("Ірина", 15)]
    print(filter_adults(people))
    # [("Андрій", 25), ("Марія", 19)]
