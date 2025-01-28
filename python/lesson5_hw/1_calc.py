import decimal

decimal.getcontext().Emax = 5
decimal.getcontext().Emin = -5


class UnknownOperationError(Exception):
    pass


class Calc:
    def __init__(self, num1, num2):
        self.num1 = decimal.Decimal(num1)
        self.num2 = decimal.Decimal(num2)

    def add(self):
        try:
            return self.num1 + self.num2
        except decimal.Overflow:
            raise OverflowError("Result of addition caused an overflow")

    def sub(self):
        try:
            return self.num1 - self.num2
        except decimal.Overflow:
            raise OverflowError("Result of subtraction caused an overflow")

    def mult(self):
        try:
            return self.num1 * self.num2
        except decimal.Overflow:
            raise OverflowError("Result of multiplication caused an overflow")

    def div(self):
        if self.num2 == 0:
            raise ZeroDivisionError("Second argument cannot be 0")
        try:
            return self.num1 / self.num2
        except decimal.Overflow:
            raise OverflowError("Result of division caused an overflow")


def run_calculation(calculator, num1, num2, action):
    calc = calculator(num1, num2)

    if action == "+":
        return calc.add()
    elif action == "-":
        return calc.sub()
    elif action == "*":
        return calc.mult()
    elif action == "/":
        return calc.div()
    else:
        raise UnknownOperationError("Unknown action")


if __name__ == '__main__':
    try:
        num1 = input("Enter first value: ")
        num2 = input("Enter second value: ")
        action = input("Choose action (+, -, *, /): ").strip()
        print(run_calculation(Calc, num1, num2, action))
    except (ValueError, decimal.InvalidOperation):
        print(
            "(ValueError) - Invalid number input. Please enter a valid "
            "numeric value.")
    except ZeroDivisionError as e:
        print(f"(ZeroDivisionError) - {e}")
    except OverflowError as e:
        print(f"(OverflowError) - {e}")
    except UnknownOperationError as e:
        print(f"(UnknownOperationError) - {e}")
