# 1.	Реалізуйте клас Vector, що підтримує операції додавання, віднімання,
# множення на число та порівняння за довжиною. Використовуйте відповідні
# dunder-методи (__add__, __sub__, __mul__, __lt__, __eq__).
# 2.	Додайте до класу метод для отримання довжини вектора.


class Vector:
    """Class for vector operations. Add, subtract, multiply, compare."""

    def __init__(self, x: int, y: int):

        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Invalid values. Should be integers.")
        self.x = x
        self.y = y

    @classmethod
    def _verify_data(cls, other: (int, "Vector")):
        if not isinstance(other, (int, Vector)):
            raise ValueError("Invalid values.")

    def __add__(self, other: (int, "Vector")):
        """Adds two vectors together or add value to vector coordinates."""

        self._verify_data(other)
        if isinstance(other, Vector):
            x = self.x + other.x
            y = self.y + other.y
            return Vector(x, y)
        elif isinstance(other, int):
            x = self.x + other
            y = self.y + other
            return Vector(x, y)

    def __radd__(self, other: int):
        """Add value to vector coordinates if value is on the left side."""
        return self + other

    def __sub__(self, other: (int, "Vector")):
        """Subs two vectors together or subs value from vector coordinates."""

        self._verify_data(other)
        if isinstance(other, Vector):
            x = self.x - other.x
            y = self.y - other.y
            return Vector(x, y)
        elif isinstance(other, int):
            x = self.x - other
            y = self.y - other
            return Vector(x, y)

    def __rsub__(self, other: (int, "Vector")):
        """Subs  if value is on the left side."""

        self._verify_data(other)
        if isinstance(other, Vector):
            x = other.x - self.x
            y = other.y - self.y
            return Vector(x, y)
        elif isinstance(other, int):
            x = other - self.x
            y = other - self.y
            return Vector(x, y)

    def __mul__(self, other: (int, "Vector")):
        """Multiply two vectors together or multiply value to vector
        coordinates."""
        self._verify_data(other)
        if isinstance(other, Vector):
            x = self.x * other.x
            y = self.y * other.y
            return Vector(x, y)
        elif isinstance(other, int):
            x = self.x * other
            y = self.y * other
            return Vector(x, y)

    def __rmul__(self, other):
        return self * other

    def __eq__(self, other: "Vector"):
        if not isinstance(other, Vector):
            raise ValueError("Invalid values.")
        else:
            return self.x == other.x and self.y == other.y

    def __lt__(self, other: "Vector"):
        if not isinstance(other, Vector):
            raise ValueError("Invalid values.")
        else:
            return self.x < other.x and self.y < other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)
print(v1 + 2)
print(2 + v1)

print(v1 - v2)
print(v1 - 3)
print(3 - v1)

print(v1 * v2)
print(v1 * 2)
print(2 * v1)

print(v1 == v2)
print(v1 < v2)
