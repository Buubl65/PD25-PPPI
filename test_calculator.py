import pytest
from calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(10, 5) == 15

def test_subtract():
    assert calc.subtract(10, 5) == 5

def test_multiply():
    assert calc.multiply(4, 3) == 12

def test_divide():
    assert calc.divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(5, 0)

def test_discount():
    assert calc.discount(100, 10) == 90
    assert calc.discount(200, 50) == 100

def test_discount_invalid():
    with pytest.raises(ValueError):
        calc.discount(100, -5)
    with pytest.raises(ValueError):
        calc.discount(100, 150)

def test_add_vat():
    assert calc.add_vat(100, 20) == 120
    assert calc.add_vat(0, 15) == 0

def test_remove_vat():
    assert round(calc.remove_vat(120, 20), 2) == 100
    assert round(calc.remove_vat(220, 10), 2) == 200
    assert calc.remove_vat(0, 15) == 0
