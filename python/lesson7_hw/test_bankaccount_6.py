"""Tests for bank account"""
from unittest.mock import MagicMock
import pytest
from bankaccount import BankAccount


@pytest.fixture
def bank_account():
    """Fixture creates bank account with 100.0"""
    return BankAccount(100.0)


@pytest.mark.parametrize("deposit_amount, expected_balance", [
    (50, 150),
    (100, 200),
    (0, 100),
])
def test_deposit(bank_account, deposit_amount, expected_balance):
    """test for deposit"""
    if deposit_amount == 0:
        with pytest.raises(ValueError,
                           match="Deposit amount must be positive"):
            bank_account.deposit(deposit_amount)
    else:
        bank_account.deposit(deposit_amount)
        assert bank_account.get_balance() == expected_balance


@pytest.mark.parametrize("withdraw_amount, expected_balance", [
    (50, 50),
    (100, 0),
    (150, -1),
])
def test_withdraw(bank_account, withdraw_amount, expected_balance):
    """test for withdraw"""
    if expected_balance < 0:
        with pytest.raises(ValueError, match="Insufficient funds"):
            bank_account.withdraw(withdraw_amount)
    else:
        bank_account.withdraw(withdraw_amount)
        assert bank_account.get_balance() == expected_balance


def test_get_balance_with_mock():
    """test get balance with mock"""
    bank_account = BankAccount()
    bank_account.get_balance = MagicMock(return_value=500.0)
    assert bank_account.get_balance() == 500.0
    bank_account.get_balance.assert_called_once()


@pytest.mark.skipif(BankAccount(0).get_balance() == 0,
                    reason="Skipping withdrawal test due to zero balance")
def test_withdraw_on_empty_account():
    """test withdraw_on_empty_account"""
    account = BankAccount(0)
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(50)


if __name__ == "__main__":
    pytest.main()
