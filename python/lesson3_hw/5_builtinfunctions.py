# 1.	Реалізуйте власну версію функцій len(), sum(), та min().
# Використовуйте спеціальні методи __len__, __iter__, __getitem__,
# якщо необхідно.
#
# 2.	Напишіть тест для кожної з реалізованих функцій.


class CustomList:
    """Class with custom methods for len(), sum(), min()."""

    def __init__(self, items: list):
        self.items = items

    def __len__(self):
        """Method for len()."""
        count = 0
        for _ in self.items:
            count += 1
        return count

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def custom_sum(self):
        """Method for sum()."""
        total = 0
        for item in self:
            total += item
        return total

    def custom_min(self):
        """Method for min()."""
        if len(self) == 0:
            raise ValueError("min() arg is an empty sequence")

        minimum = self[0]
        for item in self:
            if item < minimum:
                minimum = item
        return minimum


if __name__ == "__main__":
    numbers = CustomList([3, 1, 4, 1, 5, 9])

    print(f"Length: {len(numbers)}")  # Очікуваний результат: 6

    print(f"Sum: {numbers.custom_sum()}")  # Очікуваний результат: 23

    print(f"Min: {numbers.custom_min()}")  # Очікуваний результат: 1

    empty_list = CustomList([])
    try:
        print(empty_list.custom_min())
    except ValueError as e:
        print(f"Expected error: {e}")
