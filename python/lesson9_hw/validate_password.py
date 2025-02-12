"""Module with validate_password function"""

import re


def validate_password(psw: str) -> bool:
    """validate_password function"""
    # check length password
    if len(psw) < 8:
        print("Length of password should be at least 8 characters")
        return False

    # check digit in psw
    pattern = r"[\d]"
    result = re.search(pattern, psw)
    if not result:
        print("Password should contain at least one digit")
        return False

    # check capital digit in psw
    pattern = r"[A-Z]"
    result = re.search(pattern, psw)
    if not result:
        print("Password should contain at least one capital letter")
        return False

    # check capital digit in psw
    pattern = r"[a-z]"
    result = re.search(pattern, psw)
    if not result:
        print("Password should contain at least one lowercase letter")
        return False

    # check capital digit in psw
    pattern = r"[@#$%&_]"
    result = re.search(pattern, psw)
    if not result:
        print("Password should contain at least one special symbol")
        return False

    return True


if __name__ == "__main__":
    PSW1 = "adfsbdgd1A$"
    PSW2 = "1sadvf3$_A"

    print(validate_password(PSW1))
    print(validate_password(PSW2))
