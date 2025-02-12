"""Module with function find phone numbers"""

import re


def find_phone_numbers(input_text: str) -> list:
    """function find_phone_numbers"""
    pattern = r"\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}"
    return re.findall(pattern, input_text)


if __name__ == "__main__":
    TEXT = """
        (123) 456-7890
        123-456-7890
        123.456.7890
        1234567890
        (123) 45-7890
        1234-567-890
    """
    print(find_phone_numbers(TEXT))
