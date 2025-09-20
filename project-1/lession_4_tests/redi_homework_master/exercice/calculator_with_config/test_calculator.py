

def test_add(calculator):
    assert calculator.add(2, 3) == 5


def test_subtract(calculator):
    assert calculator.subtract(5, 3) == 2


def test_multiply(calculator):
    assert calculator.multiply(4, 3) == 12


def test_divide(calculator):
    assert calculator.divide(10, 2) == 5

