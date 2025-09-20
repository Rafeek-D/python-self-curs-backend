from lession_3_tests.account import Account

class Account:

    def __init__(self, account_number: str, initial_balance: float = 0.0) -> None:
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def get_balance(self) -> float:
        return self.balance



a1 = Account(account_number="a1", initial_balance=100)
a1.deposit(10)
#a1.deposit(-10)
#a1.withdraw("10")
#a1.withdraw(200)
print(a1.get_balance())