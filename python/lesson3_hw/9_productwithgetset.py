# Сеттери/геттери: реалізуйте методи get_price() і set_price(), які будуть
# дозволяти отримувати та встановлювати значення атрибута price. Додайте
# перевірку, що ціна не може бути від'ємною. Якщо ціна менше 0, викиньте
# виняток ValueError.

class ProductWithGetSet:
    """Class Product with get_price() and set_price() methods."""

    def __init__(self, name: str, price: float):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self._name = name
        self._price = price

    def get_price(self):
        """Getter for price."""
        return self._price

    def set_price(self, value: float):
        """Setter for price."""
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


if __name__ == "__main__":

    p1 = ProductWithGetSet("Laptop", 1000)
    print(p1.get_price())
    p1.set_price(500)
    print(p1.get_price())
    try:
        p1.set_price(-100)
    except ValueError as e:
        print(e)
