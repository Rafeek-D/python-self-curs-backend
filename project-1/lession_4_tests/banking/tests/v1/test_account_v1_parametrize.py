import pytest
#import sys

#sys.path.insert('1,/home/rafeekkali/Documents/project-1/4_test/banking/')

from lession_4_tests.banking.src.v1.account import Account


@pytest.fixture
def account() -> Account:
    return Account(account_number="123456", initial_balance=100.0)


def test_initial_balance(account: Account) -> None:
    assert account.get_balance() == 100.0


@pytest.mark.parametrize(
    "amount, error_type, error_msg",
    [
        (200.0, ValueError, "Insufficient funds."),
        (-10.0, ValueError, "Withdrawal amount must be positive."),
        ("ErrorTrigger", TypeError, "Withdrawal amount must be a number."),

    ]
)
def test_withdraw_value_errors(account: Account, error_type: Exception, amount, error_msg) -> None:
    with pytest.raises(error_type, match=error_msg):
        account.withdraw(amount)


#------raf-------------
def test_deposit_value_er(account: Account) -> None:
    with pytest.raises(ValueError, match="Deposit amount must be positive."):
        account.deposit(amount=-10.0)