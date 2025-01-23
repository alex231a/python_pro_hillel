class ProductWithDescriptor:
    """Class Product with properties price and name."""

    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    @property
    def price(self):
        """Getter for price."""
        return self._price

    @price.setter
    def price(self, value: float):
        """Setter for price."""
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @property
    def name(self):
        """Getter for name."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Setter for name."""
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value.strip()


if __name__ == "__main__":
    p1 = ProductWithDescriptor("Laptop", 1000)
    print(p1.price)
    p1.price = 500
    print(p1.price)
    try:
        p1.price = -100
    except ValueError as e:
        print(e)
