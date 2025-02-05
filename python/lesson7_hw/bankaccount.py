"""Module with class BankAccount"""


class BankAccount:
    """Class BankAccount"""
    def __init__(self, initial_balance=0.0):
        self.balance = initial_balance

    def deposit(self, amount: float):
        """method deposit"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float):
        """method withdraw"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self) -> float:
        """method get_balance"""
        return self.balance
