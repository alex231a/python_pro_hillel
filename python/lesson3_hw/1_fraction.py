# 1.	Реалізуйте клас Fraction (дробові числа), який має методи для
# додавання, віднімання, множення та ділення двох об'єктів цього класу.
# Використайте спеціальні методи __add__, __sub__, __mul__, __truediv__.
# 2.	Реалізуйте метод __repr__, щоб можна було коректно виводити об'єкти
# цього класу у форматі "numerator/denominator".

class Fraction:
    """Class representing a fraction. Have methods for adding, subtracting,
    multiplying and dividing two fractions."""

    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Denominator cannot be 0")
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError("Numerator and denominator must be integers")

        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other: "Fraction"):
        """Adds two fractions together."""

        self._check_if_instance_belongs_to_class(other)
        numerator = (self.numerator * other.denominator + self.denominator *
                     other.numerator)
        denominator = self.denominator * other.denominator

        numerator, denominator = self._reduce_fraction(numerator, denominator)

        return Fraction(numerator, denominator)

    def __sub__(self, other: "Fraction"):
        """Subtracts two fractions."""

        self._check_if_instance_belongs_to_class(other)
        numerator = (self.numerator * other.denominator - self.denominator *
                     other.numerator)
        denominator = self.denominator * other.denominator
        numerator, denominator = self._reduce_fraction(numerator, denominator)

        return Fraction(numerator, denominator)

    def __mul__(self, other: "Fraction"):
        """Multiplies two fractions."""

        self._check_if_instance_belongs_to_class(other)
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        numerator, denominator = self._reduce_fraction(numerator, denominator)

        return Fraction(numerator, denominator)

    def __truediv__(self, other: "Fraction"):
        """Divides two fractions."""

        self._check_if_instance_belongs_to_class(other)
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        numerator, denominator = self._reduce_fraction(numerator, denominator)
        return Fraction(numerator, denominator)

    @classmethod
    def _check_if_instance_belongs_to_class(cls, instance: "Fraction"):
        """Checks if the instance belongs to the class."""

        if not isinstance(instance, cls):
            raise ValueError(
                "Instance does not belong to the class." + __class__.__name__)
        return True

    @staticmethod
    def _reduce_fraction(numerator: int, denominator: int):
        """Reduces a fraction to its simplest form."""
        step = 2
        while step <= 5:
            if numerator % step != 0 or denominator % step != 0:
                step += 1
            else:
                numerator = int(numerator / step)
                denominator = int(denominator / step)
        return numerator, denominator

    def __repr__(self):
        """Returns the representation of the fraction."""
        if self.denominator == 1:
            return f"{self.numerator}"
        return f"{self.numerator}/{self.denominator}"


f1 = Fraction(1, 2)
f2 = Fraction(1, 4)

f3 = f1 + f2
f4 = f1 - f2
f5 = f1 * f2
f6 = f1 / f2
print(f3)
print(f4)
print(f5)
print(f6)
