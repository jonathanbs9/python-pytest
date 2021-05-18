""" 
This module contains  basic unit tests for math operations.
Their purpose is to show how to use the pytest framework by example.
"""
# ----------
# Imports 
# ----------
import pytest

# ----------------------
# Basic test function
# ----------------------

@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2

# Chapter 2 - Failing test case
@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c

# Chapter 3 - Test case with an Exception
@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        number = 1 / 0
    assert 'division by zer' in str(e.value)

# Chapter 4 -  Parametrized Test Case

# Multiplication test ideas
    # 2 positive integers
    # identity: multiplying any number by 1
    # zero: multiplying any number by 0
    # positive by a negative
    # negative by a negative
    # multiply floats
products = [
    (2, 3, 6),          # positive integers
    (1, 99, 99),        # Identity
    (0, 99, 0),         # Zero
    (2, -3, -6),        # Positive by a negative
    (-3, -3, 9),        # Negative by a negative
    (2.5, 6.7, 16.75)   # Floats
]

@pytest.mark.math
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product

def test_multiply_two_positive_integers():
    assert 2 * 30 == 60

def  test_multiply_identity():
    assert 1 * 99 == 99

def test_multiply_zero():
    assert 0 * 00 == 0

# Chapter 5 - Testing Classes
