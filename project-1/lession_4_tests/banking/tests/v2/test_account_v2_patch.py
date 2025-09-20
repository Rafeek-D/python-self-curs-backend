import pytest
from unittest.mock import MagicMock

from banking.src.v2.account import Account

@pytest.fixture
def mock_db():
    mock = MagicMock()
    mock.save_account.return_value = True
    mock.get_account.return_value = 100.0
    return mock

@pytest.fixture
def account(mock_db):
    acc = Account(account_number="MOCK456", initial_balance=100.0, db_connection=mock_db)
    acc.db_connection = mock_db
    return acc

def test_deposit_calls_save_account(account, mock_db):
    account.deposit(25.0)
    mock_db.save_account.assert_called_with("MOCK456", 125.0)

def test_withdraw_calls_save_account(account, mock_db):
    account.withdraw(50.0)
    mock_db.save_account.assert_called_with("MOCK456", 50.0)

def test_get_balance_calls_save_account(account, mock_db):
    account.get_balance()
    mock_db.save_account.assert_called_with("MOCK456")

