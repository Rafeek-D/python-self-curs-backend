class DatabaseConnection:
    def __init__(self, db_url):
        raise ConnectionError("Failed to connect to the database.")

    def save_account(self, account_number: str, balance: float) -> None:
        pass

    def get_account(self, account_number: str) -> float:
        pass
