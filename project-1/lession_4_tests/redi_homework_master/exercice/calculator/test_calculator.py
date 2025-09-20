import pytest

from calculator import Calculator

calculator_fixture_scope = "placeholder"  # TODO (5 Points) add the correct scope here


@pytest.fixture(scope=calculator_fixture_scope)
def calculator():
    return Calculator()


def test_add(calculator):
    """Example: Test subtraction operation."""
    assert calculator.add(2, 3) == 5


def test_subtract(calculator):
    """Example: Test subtraction operation."""
    assert calculator.subtract(5, 3) == 2


def test_multiply(calculator):
    # TODO (5 Points) : Complete this test
    pass


def test_divide(calculator):
    # TODO (5 Points) : Complete this test
    pass


def test_divide_by_zero(calculator):
    # TODO (10 Points) : Complete this test (Hint: use pytest.raises)
    pass


def test_evaluate_add(calculator):
    assert calculator.evaluate(2, 3, "add") == 5


def test_evaluate_subtract(calculator):
    assert calculator.evaluate(5, 3, "subtract") == 2


def test_evaluate_multiply(calculator):
    assert calculator.evaluate(4, 3, "multiply") == 12


def test_evaluate_divide(calculator):
    assert calculator.evaluate(10, 2, "divide") == 5


def test_evaluate(calculator, a, b, op, expected):
    """
    TODO (20 Points) : Add the @pytest.mark.parametrize decorator to test multiple operations in one go,
    allowing to replace the individual tests above. (test_evaluate_add, test_evaluate_subtract...)
    """

    assert calculator.evaluate(a, b, op) == expected


