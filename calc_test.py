
import pytest

from calc import add, substract, multiply, division

def test_add():
    assert add(6, 2) == 8

def test_sub():
    assert substract(6, 2) == 4

def test_mul():
    assert multiply(2, 3) == 6

def test_div():
    assert division(12, 3) == 4