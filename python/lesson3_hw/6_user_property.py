# 1.	Реалізуйте клас User з атрибутами first_name, last_name, email.
# Додайте методи для отримання та встановлення цих атрибутів через декоратор
# @property.
#
# 2.	Додайте методи для перевірки формату email-адреси.

import re


class User:
    """Class User with properties first_name, last_name, email."""

    def __init__(self, first_name: str, last_name: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @property
    def first_name(self):
        """Getter for first_name."""
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        """Setter for first_name."""
        if not isinstance(value, str):
            raise ValueError("First name must be a string.")
        self.__first_name = value.strip()

    @property
    def last_name(self):
        """Getter for last_name."""
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        """Setter for last_name."""
        if not isinstance(value, str):
            raise ValueError("First name must be a string.")
        self.__last_name = value.strip()

    @property
    def email(self):
        """Getter for email."""
        return self.__email

    @email.setter
    def email(self, value):
        """Setter for email."""
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_pattern, value):
            raise ValueError("Invalid email address")
        self.__email = value.strip()

    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"


if __name__ == "__main__":
    user1 = User("John", "Smith", "test@gmail.com")
    print(user1)
    try:
        user2 = User('Jim', "Dou", "123")
    except ValueError as e:
        print(f"You entered {e} for new object of User class.")
