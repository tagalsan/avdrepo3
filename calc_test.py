
import pytest

from calc.py import add, substract, multiply, division

def test_add():
    assert add(2, 3) == 5