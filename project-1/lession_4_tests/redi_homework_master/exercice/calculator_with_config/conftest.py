import pytest
from unittest.mock import MagicMock
from ...exercice.calculator_with_config.calculator import Calculator

@pytest.fixture
def config():
    """
    TODO (25 Points) : Complete this fixture to return a MagicMock object.
    The Mock object should have a method get_prompt that returns the string ">".
    """
    pass

@pytest.fixture
def calculator(config):
    return Calculator(config=config)

