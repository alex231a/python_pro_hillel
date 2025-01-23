# 1.	Реалізуйте клас Person із параметрами name та age. Додайте методи для
# порівняння за віком (__lt__, __eq__, __gt__).
# 2.	Напишіть програму для сортування списку об'єктів класу Person за
# віком.


class Person:
    """Class Person. Have methods for comparing by age."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @classmethod
    def _verify_data(cls, other: (int, "Person")):
        """Verifies if the data is valid."""

        if not isinstance(other, (int, Person)):
            raise ValueError("Invalid values.")

    def __lt__(self, other: (int, "Person")):
        """Compares by age, less than."""
        self._verify_data(other)
        if isinstance(other, Person):
            return self.age < other.age
        elif isinstance(other, int):
            return self.age < other

    def __eq__(self, other: (int, "Person")):
        """Compares by age, equals."""

        self._verify_data(other)
        if isinstance(other, Person):
            return self.age == other.age
        elif isinstance(other, int):
            return self.age == other

    def __gt__(self, other: (int, "Person")):
        """Compares by age, greater than."""

        self._verify_data(other)
        if isinstance(other, Person):
            return self.age > other.age
        elif isinstance(other, int):
            return self.age > other

    def __repr__(self):
        return f"{self.name} ({self.age})"


people = [
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35),
    Person("David", 20)
]

sorted_people = sorted(people)
print(sorted_people)
