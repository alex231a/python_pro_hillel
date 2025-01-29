class InsufficientFundsException(Exception):
    """Custom Exception. Raises if client has insufficient credits"""

    def __init__(self, required_amount: float, current_balance: float,
                 currency: str, transaction_type: str):
        self.required_amount = required_amount
        self.current_balance = current_balance
        self.currency = currency
        self.transaction_type = transaction_type

    def __str__(self):
        return (
            f"ERROR. Insufficient credits. Transaction type is "
            f"{self.transaction_type}. Required amount is "
            f"{self.required_amount}, Current balance is "
            f"{self.current_balance}, Currency is {self.currency}.")


class Client:
    """Class that represents client"""

    def __init__(self, name: str, balance: float, currency: str = "USD"):
        self._name = name
        self._balance = balance
        self._currency = currency

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    def get_balance(self):
        return self._balance

    def set_balance(self, amount: float):
        self._balance = self._balance - amount

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, new_value: str):
        self._currency = new_value

    def __str__(self):
        return f"Client {self.name} has {self.get_balance()} {self.currency}"


class Actions:
    """Class that represents actions with client balance"""

    def __init__(self, client: Client):
        self.client = client

    def operation(self, operation_name: str, amount: float):
        """Method for withdrawal ir purchase"""
        try:
            if operation_name not in ["withdrawal", "purchase"]:
                raise TypeError("Error. Unknown operation")
            if amount > self.client.get_balance():
                raise InsufficientFundsException(amount,
                                                 self.client.get_balance(),
                                                 self.client.currency,
                                                 operation_name)
            self.client.set_balance(amount)
            print(
                f"Success with {operation_name} operation. "
                f"{self.client.name} got {amount}. Account balance "
                f"is {self.client.get_balance()} {self.client.currency}")
        except (InsufficientFundsException, TypeError) as e:
            print(e)


if __name__ == "__main__":
    client = Client("Bob Singer", 3500)
    print(client)

    actions = Actions(client)
    actions.operation("withdrawal", 1000)
    actions.operation("purchase", 1000)
    actions.operation("withdrawal", 3000)
    actions.operation("cash", 3000)
