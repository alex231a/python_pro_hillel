# 1.	Реалізуйте клас BinaryNumber, який представляє двійкове число.
# Додайте методи для виконання двійкових операцій: AND (__and__),
# OR (__or__), XOR (__xor__) та NOT (__invert__).
#
# 2.	Напишіть тест для цих операцій.


class BinaryNumber:
    """Class for binary numbers. Have methods for AND, OR, XOR, NOT."""

    def __init__(self, value: str):
        if not all(c in "01" for c in value):
            raise ValueError("Value must be a binary string.")
        self.value = value

    def __str__(self):
        return self.value

    def __and__(self, other: "BinaryNumber"):
        """Method for AND operation."""
        result = bin(int(self.value, 2) & int(other.value, 2))[2:]
        return BinaryNumber(
            result.zfill(max(len(self.value), len(other.value))))

    def __or__(self, other: "BinaryNumber"):
        """Method for OR operation."""
        result = bin(int(self.value, 2) | int(other.value, 2))[2:]
        return BinaryNumber(
            result.zfill(max(len(self.value), len(other.value))))

    def __xor__(self, other: "BinaryNumber"):
        """Method for XOR operation."""
        result = bin(int(self.value, 2) ^ int(other.value, 2))[2:]
        return BinaryNumber(
            result.zfill(max(len(self.value), len(other.value))))

    def __invert__(self: "BinaryNumber"):
        """Method for NOT operation."""
        inverted = ''.join('1' if c == '0' else '0' for c in self.value)
        return BinaryNumber(inverted)


if __name__ == "__main__":
    a = BinaryNumber("1010")
    b = BinaryNumber("1100")

    print(f"a: {a}")
    print(f"b: {b}")

    # AND
    and_result = a & b
    print(f"a & b: {and_result}")

    # OR
    or_result = a | b
    print(f"a | b: {or_result}")

    # XOR
    xor_result = a ^ b
    print(f"a ^ b: {xor_result}")

    # NOT
    not_a = ~a
    print(f"~a: {not_a}")
