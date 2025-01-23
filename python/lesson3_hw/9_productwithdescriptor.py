from decimal import Decimal, ROUND_HALF_UP
from typing import Union, Tuple


class PriceDescriptor:
    """Class PriceDescriptor for setting and getting price."""

    def __get__(self, instance, owner):
        """Getter for price."""
        return instance.__dict__.get("price")

    def __set__(self, instance, value):
        """Setter for price."""
        if float(value) < 0:
            raise ValueError("Price cannot be negative")
        instance.__dict__["price"] = value


class CurrencyDescriptor:
    """Descriptor for converting currency"""
    exchange_rates = {
        'USD': Decimal('1.00'),
        'EUR': Decimal('0.96')
    }

    def __init__(self, default_currency: str = 'USD'):
        if default_currency not in self.exchange_rates:
            raise ValueError(f"Unsupported currency: {default_currency}")
        self.default_currency = default_currency
        self._value = Decimal('0.00')

    def __get__(self, instance, owner):
        return float(self._value)

    def __set__(self, instance,
                value: Union[Tuple[str, Union[float, int, str]], Decimal]):
        """Set price in chosen currency."""
        if isinstance(value, tuple):
            currency, amount = value
        else:
            raise ValueError("Expected a tuple with currency and amount.")

        if currency not in self.exchange_rates:
            raise ValueError(f"Unsupported currency: {currency}")

        try:
            amount = Decimal(amount)
        except (ValueError, TypeError):
            raise ValueError("Price must be a numeric value.")

        if amount < 0:
            raise ValueError("Price cannot be negative.")

        self._value = (amount / self.exchange_rates[currency]).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP)


class ProductWithDescriptor:
    """Class product with descriptors price and currency_price."""
    price = PriceDescriptor()
    currency_price = CurrencyDescriptor()

    def __init__(self, name: str, price: Union[float, int, str],
                 currency: str = 'USD'):
        self.name = name
        self.price = price
        self.currency_price = (currency, Decimal(price))

    def __str__(self) -> str:
        return (f"Product(name={getattr(self, 'name', 'Unknown')}, price=$"
                f"{float(self.price):.2f}, price"
                f" in EUR={float(self.get_price_in_eur()):.2f}€)")

    def get_price_in_usd(self):
        """Get Price in USD."""
        return self.currency_price

    def get_price_in_eur(self):
        """Get Price in EUR."""
        return Decimal(self.currency_price) * \
            CurrencyDescriptor.exchange_rates['EUR']


if __name__ == "__main__":
    p1 = ProductWithDescriptor("Laptop", 1000)

    print(p1.price)
    p1.price = 500
    print(p1.price)
    try:
        p1.price = -100
    except ValueError as e:
        print(e)
    print(p1)

    p = ProductWithDescriptor("Phone", 499.99, "USD")
    print(p)
    p.currency_price = ("EUR", 200)
    print(p.get_price_in_usd())

    p.price = "599.95"
    print(p)
