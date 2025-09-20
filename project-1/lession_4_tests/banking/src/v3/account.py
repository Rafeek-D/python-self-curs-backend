from banking.src.v3.database import DatabaseConnection
from banking.src.v3.user import User


class Account:
    def __init__(self, account_number: str, user: User, initial_balance: float = 0.0, db_connection=None) -> None:
        self.db_connection = db_connection if db_connection is not None else DatabaseConnection("db_url")
        self.user = user
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.db_connection.save_account(self.account_number, self.balance)

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.db_connection.save_account(self.account_number, self.balance)

    def get_balance(self) -> float:
        db_balance = self.db_connection.get_account(self.account_number)
        return self.balance

    def get_owner(self) -> User:
        return self.user