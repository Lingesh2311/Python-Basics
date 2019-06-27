'''
This is the test function using pytest framework
'''
import math_func


def test_add():
    assert math_func.add(7, 1) == 11
    assert math_func.add(8, 2, 3) == 13


def test_prod():
    assert math_func.mul(8) == 8
    assert math_func.mul(8, 2) == 16
