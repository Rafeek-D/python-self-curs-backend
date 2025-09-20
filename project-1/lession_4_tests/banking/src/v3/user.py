from banking.src.v3.database import DatabaseConnection


class User:
    def __init__(self, user_id, name: str, db_connection=None) -> None:
        self.name = name
        self.user_id = user_id
        self.db_connection = db_connection if db_connection is not None else DatabaseConnection("db_url")

    def get_user_info(self):
        return {"user_id": self.user_id, "name": self.name}
