"""Module with function that converts date format from DD/MM/YYYY to
YYYY-MM-DD"""

import re


def format_date(string_date: str) -> str:
    """Function that converts date format from DD/MM/YYYY to YYYY-MM-DD"""
    pattern = r"(\d{2})/(\d{2})/(\d{4})"
    result = re.search(pattern, string_date)
    if result:
        day = result.group(1)
        month = result.group(2)
        year = result.group(3)
        return f"{year}-{month}-{day}"
    return "Wrong format of input date string."


if __name__ == "__main__":
    DT_STR1 = "12/05/2024"
    DT_STR2 = "21-05-2024"
    DT_STR3 = "12_05_2024"

    print(format_date(DT_STR1))
    print(format_date(DT_STR2))
    print(format_date(DT_STR3))
