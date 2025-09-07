import pytest
from fibonacci import fibonacci

def test_fibonacci_zero():
    assert fibonacci(0) == 0

def test_fibonacci_one():
    assert fibonacci(1) == 1

def test_fibonacci_five():
    assert fibonacci(5) == 5

def test_fibonacci_negative():
    try:
        fibonacci(-1)
        assert False, "Expected ValueError"
    except ValueError:
        assert True
