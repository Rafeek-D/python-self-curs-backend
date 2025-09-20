import pytest
from banking.src.v3.account import Account
from banking.src.v3.user import User

@pytest.fixture
def user(mock_db):
    return User(user_id=1, name="Alice", db_connection=mock_db)

@pytest.fixture
def account(user, mock_db):
    return Account(account_number="ACC123", user=user, initial_balance=100.0, db_connection=mock_db)

def test_deposit(account, mock_db):
    account.deposit(50)
    mock_db.save_account.assert_called_with("ACC123", 150.0)

def test_withdraw(account, mock_db):
    account.withdraw(30)
    mock_db.save_account.assert_called_with("ACC123", 70.0)

def test_withdraw_insufficient_funds(account):
    with pytest.raises(ValueError, match="Insufficient funds."):
        account.withdraw(200)

def test_get_balance(account, mock_db):
    balance = account.get_balance()
    mock_db.get_account.assert_called_with("ACC123")
    assert balance == 100.0
