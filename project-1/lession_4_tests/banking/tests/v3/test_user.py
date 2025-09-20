from banking.src.v3.user import User


def test_user_info(mock_db):
    user = User(user_id=2, name="Bob", db_connection=mock_db)
    info = user.get_user_info()
    assert info == {"user_id": 2, "name": "Bob"}
