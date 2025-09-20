import pytest

from lession_4_tests.banking.src.v1.account import Account

# Function-scoped fixture: new Account for each test
@pytest.fixture(scope="function")
def func_account():
    return Account(account_number="FUNC", initial_balance=100.0)

# Class-scoped fixture: shared Account for all tests in the class
@pytest.fixture(scope="class")
def class_account():
    return Account(account_number="CLASS", initial_balance=100.0)

# Module-scoped fixture: shared Account for all tests in the module
@pytest.fixture(scope="module")
def module_account():
    return Account(account_number="MODULE", initial_balance=100.0)

def test_func_scope_1(func_account):
    func_account.deposit(50)
    assert func_account.get_balance() == 150.0

def test_func_scope_2(func_account):
    # Should not be affected by previous test
    assert func_account.get_balance() == 100.0

class TestClassScope:
    def test_class_scope_1(self, class_account):
        class_account.deposit(30)
        assert class_account.get_balance() == 130.0

    def test_class_scope_2(self, class_account):
        # State persists from previous test in the class
        class_account.withdraw(10)
        assert class_account.get_balance() == 120.0

def test_module_scope_1(module_account):
    module_account.deposit(20)
    assert module_account.get_balance() == 120.0

def test_module_scope_2(module_account):
    # State persists from previous test in the module
    module_account.withdraw(10)
    assert module_account.get_balance() == 110.0

