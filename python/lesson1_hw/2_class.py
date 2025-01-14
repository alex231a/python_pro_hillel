class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

    def __str__(self):
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

