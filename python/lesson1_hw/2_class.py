class Rectangle:
    """class that represents rectangle. Have methods for getting area,
    perimeter, is_square and resize"""
    def __init__(self, width: float, height: float):
        """
        Initialize a rectangle with width and height.
        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        """
        self.width: float = width
        self.height: float = height

    def area(self) -> float:
        """
        Calculate the area of the rectangle.
        :return: The area as a float.
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle.
        :return: The perimeter as a float.
        """
        return 2 * (self.width + self.height)

    def is_square(self) -> bool:
        """
        Check if the rectangle is a square.
        :return: True if it is a square, False otherwise.
        """
        return self.width == self.height

    def resize(self, new_width, new_height) -> None:
        """
        Resize the rectangle to new dimensions.
        :param new_width: The new width of the rectangle.
        :param new_height: The new height of the rectangle.
        """
        self.width = new_width
        self.height = new_height

    def __str__(self) -> str:
        """
        Return a string representation of the rectangle.
        :return: A string with the rectangle's dimensions.
        """
        return f"Rectangle(width={self.width}, height={self.height})"


test_rectangle = Rectangle(10, 5)
print(test_rectangle.__str__())
print(f"Rectangle area is {test_rectangle.area()}")
print(f"Rectangle perimeter is {test_rectangle.perimeter()}")
print(f"Is the rectangle a square? {test_rectangle.is_square()}")

print("")
print("")

test_rectangle.resize(100, 20)
print(test_rectangle.__str__())
print(f"Rectangle new area is {test_rectangle.area()}")
print(f"Rectangle new perimeter is {test_rectangle.perimeter()}")
print(f"Is the new rectangle a square? {test_rectangle.is_square()}")
