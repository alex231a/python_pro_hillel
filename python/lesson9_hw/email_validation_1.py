"""Module with validate_email function"""
import re


def validate_email(email: str) -> bool:
    """Validate_email function"""
    pattern = (r"^[a-zA-Z0-9][a-zA-Z0-9.]*[a-zA-Z0-9]@[a-zA-Z0-9]+\.[a-zA-Z]{"
               r"2,6}$")
    return bool(re.match(pattern, email))


if __name__ == "__main__":
    email_list = [
        "user@example.com",
        "john.doe@domain.net",
        "test123@SubDomain.org",
        ".user@example.com",
        "user.@example.com",
        "user@domain.abcdefg",
        "user@domain.c",
        "user@dom_ain.com"
    ]
    check_list = [validate_email(email) for email in email_list]
    print(check_list)
