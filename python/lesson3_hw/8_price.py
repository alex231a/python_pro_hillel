# 1.	Реалізуйте клас Price, що представляє ціну товару з можливістю
# заокруглення до двох десяткових знаків. Додайте методи для додавання,
# віднімання та порівняння цін.
#
# 2.	Поміркуйте, як клас Price може бути використаний в майбутньому класі
# PaymentGateway для обробки фінансових транзакцій.

from decimal import Decimal, ROUND_HALF_UP


class Price:
    """Class Price for price with rounding to 2 decimal places."""

    def __init__(self, amount: (float, int, str)):
        self.amount = self.validate_and_round(amount)

    @staticmethod
    def validate_and_round(value: (float, int, str)):
        """Check and round value to 2 decimal places."""
        try:
            value = Decimal(value)
        except (ValueError, TypeError):
            raise ValueError("Price must be a numeric value.")

        if value < 0:
            raise ValueError("Price cannot be negative.")

        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    @staticmethod
    def _verify_data(self, other: "Price"):
        """Verifies if the instance belongs to the same class."""
        if not isinstance(other, Price):
            raise ValueError("Invalid values. Should be a Price.")

    def __add__(self, other: "Price"):
        """Method for adding two Price instances."""
        self._verify_data(self, other)
        return Price(self.amount + other.amount)

    def __sub__(self, other: "Price"):
        """Method for subtracting two Price instances."""
        self._verify_data(self, other)
        result = self.amount - other.amount
        if result < 0:
            raise ValueError("Price cannot be negative after subtraction.")
        return Price(result)

    def __eq__(self, other: "Price"):
        """Method for comparing two Price instances. equal."""
        self._verify_data(self, other)
        return self.amount == other.amount

    def __lt__(self, other: "Price"):
        """Method for comparing two Price instances. less than."""
        self._verify_data(self, other)
        return self.amount < other.amount

    def __le__(self, other: "Price"):
        """Method for comparing two Price instances. less than or equal."""
        self._verify_data(self, other)
        return self.amount <= other.amount

    def __gt__(self, other: "Price"):
        """Method for comparing two Price instances. greater than."""
        self._verify_data(self, other)
        return self.amount > other.amount

    def __ge__(self, other: "Price"):
        """Method for comparing two Price instances. greater than or equal."""
        self._verify_data(self, other)
        return self.amount >= other.amount

    def __repr__(self) -> str:
        """Method for representation."""
        return f"Price({self.amount:.2f})"

    def __str__(self) -> str:
        """Method for string representation."""
        return f"${self.amount:.2f}"


if __name__ == "__main__":
    p1 = Price(19.999)
    p2 = Price("10.499")
    p3 = Price(5)

    print(p1)
    print(p2)
    print(p1 + p2)
    print(p1 - p3)

    print(p1 == p2)
    print(p1 > p2)
    print(p3 < p2)
