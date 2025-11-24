import pytest
from calculator import divide

def test_divide_basic():
    assert divide(10, 2) == 5     #Prueba de lógica

def test_divide_zero():
    try:
        resultado = divide(10, 0)
        assert resultado is None
    except ZeroDivisionError:
        pytest.fail()
