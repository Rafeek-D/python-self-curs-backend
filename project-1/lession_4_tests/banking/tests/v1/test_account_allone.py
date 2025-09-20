import pytest

from lession_4_tests.banking.src.v1.account import Account

def test_account_allone():
    a1=Account(account_number="123456", initial_balance=0.0)
    a1.deposit(20)
    assert a1.get_balance() == 20