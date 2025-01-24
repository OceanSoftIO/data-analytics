import pytest
from runbooks.calculator import Calculator
from runbooks.exceptions import CalculatorError


@pytest.fixture
def calc():
    return Calculator(precision=3)  # Custom precision for tests


def test_add(calc):
    assert calc.add(2.345, 3.456) == 5.801


def test_subtract(calc):
    assert calc.subtract(5.123, 2.123) == 3.000


def test_multiply(calc):
    assert calc.multiply(3.14, 2) == 6.28


def test_divide(calc):
    assert calc.divide(10, 2) == 5


def test_divide_by_zero(calc):
    with pytest.raises(CalculatorError):
        calc.divide(1, 0)
