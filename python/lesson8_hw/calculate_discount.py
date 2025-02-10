"""Module with function calculate_discount"""


def calculate_discount(price: float, discount: float) -> float:
    """Function counts discount"""
    if discount >= 100:
        return 0.0
    return price - ((price * discount) / 100)


if __name__ == "__main__":
    print(calculate_discount(100, 20))
    print(calculate_discount(50, 110))
