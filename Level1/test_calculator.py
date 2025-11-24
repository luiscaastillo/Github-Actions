import pytest
from calculator import divide

def test_divide_basic():
    assert divide(10, 2) == 5

def test_divide_zero():
    assert divide(10, 0) is None
