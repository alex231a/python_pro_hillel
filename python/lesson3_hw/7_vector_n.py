# # 1.	Створіть клас Vector, який представляє вектор у просторі з n
# # вимірами. Додайте методи для додавання, віднімання векторів та обчислення
# # скалярного добутку. Використовуйте dunder-методи (__add__, __sub__,
# __mul__).
# #
# # 2.	Додайте можливість порівняння двох векторів за їх довжиною.
#
#

import math


class Vector:
    """Class for vector operations. Add, subtract, multiply, compare."""

    def __init__(self, *coordinates: int):
        if len(coordinates) < 2:
            raise ValueError(
                "Invalid values. Should be at least two coordinates.")
        self.coordinates = [int(point) for point in coordinates]

    def _verify_data(self, other: "Vector"):
        """Verifies if the instance belongs to the same class and has the
        same dimensions."""
        if not isinstance(other, Vector):
            raise ValueError("Invalid values. Should be a vector.")
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError(
                "Invalid values. Vectors should have the same dimensions.")

    def __add__(self, other: "Vector"):
        """Adds two vectors together"""

        self._verify_data(other)
        coordinates = [a + b for a, b in
                       zip(self.coordinates, other.coordinates)]
        return Vector(*coordinates)

    def __sub__(self, other: "Vector"):
        """Subs two vectors together."""

        self._verify_data(other)
        coordinates = [a - b for a, b in
                       zip(self.coordinates, other.coordinates)]
        return Vector(*coordinates)

    def __mul__(self, other: "Vector"):
        """Multiply two vectors"""
        self._verify_data(other)
        coordinates = [a * b for a, b in
                       zip(self.coordinates, other.coordinates)]
        return Vector(*coordinates)

    def __len__(self):
        """Returns the number of coordinates"""
        return len(self.coordinates)

    def magnitude(self):
        """Returns the magnitude of the vector."""
        return math.sqrt(sum(coord ** 2 for coord in self.coordinates))

    def __eq__(self, other: "Vector"):
        """Returns True if the magnitudes are equal."""

        self._verify_data(other)
        return math.isclose(self.magnitude(), other.magnitude())

    def __lt__(self, other: "Vector"):
        """Returns True if the magnitude of self is less than the magnitude"""
        self._verify_data(other)
        return self.magnitude() < other.magnitude()

    def __gt__(self, other: "Vector"):
        """Returns True if the magnitude of self is greater than the
        magnitude"""
        self._verify_data(other)
        return self.magnitude() > other.magnitude()

    def __repr__(self):
        return f"Vector{self.coordinates}"


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    v3 = Vector(1, 2, 3)

    print(v1)
    print(v2)
    print(v3)
    print()
    print("v1 + v2 =", v1 + v2)
    print("v2 - v1 =", v2 - v1)
    print("v1 * v2 =", v1 * v2)
    print()
    print("v1 == v3:", v1 == v3)
    print("v1 < v2:", v1 < v2)
    print("v1 > v2:", v1 > v2)
    print("Magnitude of v1:", v1.magnitude())
