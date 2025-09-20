import pytest
from unittest.mock import MagicMock


@pytest.fixture(scope='module')
def mock_db():
    mock_db = MagicMock()
    mock_db.save_account.return_value = True
    yield mock_db
