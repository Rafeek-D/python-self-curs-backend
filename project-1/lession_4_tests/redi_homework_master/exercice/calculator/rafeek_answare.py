import pytest

from lession_4_tests.redi_homework_master.exercice.calculator.calculator import Calculator

calculator_fixture_scope = "function"  # TODO (5 Points) add the correct scope here


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
    assert calculator.multiply(2, 3) == 6
    #pass


def test_divide(calculator):
    # TODO (5 Points) : Complete this test
    assert calculator.divide(6, 2) == 3.0
    #pass


def test_divide_by_zero(calculator):
    # TODO (10 Points) : Complete this test (Hint: use pytest.raises)
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calculator.divide(0, 0)
    pass


def test_evaluate_add(calculator):
    assert calculator.evaluate(2, 3, "add") == 5


def test_evaluate_subtract(calculator):
    assert calculator.evaluate(5, 3, "subtract") == 2


def test_evaluate_multiply(calculator):
    assert calculator.evaluate(4, 3, "multiply") == 12


def test_evaluate_divide(calculator):
    assert calculator.evaluate(10, 2, "divide") == 5



@pytest.mark.parametrize(
    "num1, b, op, expected",
    [
        (5, 10, "multiply" , 50)
    ]
)
def test_evaluate(calculator, num1 , b , op, expected):
    """
    TODO (20 Points) : Add the @pytest.mark.parametrize decorator to test multiple operations in one go,
    allowing to replace the individual tests above. (test_evaluate_add, test_evaluate_subtract...)
    """
    assert calculator.evaluate(num1, b, op) == expected

'''
'''