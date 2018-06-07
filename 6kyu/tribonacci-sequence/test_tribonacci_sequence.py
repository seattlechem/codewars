"""Tribonacci test cases."""
from tribonacci_sequence import tribonacci


def test_simple():
    """Test the result of simple tribonacci."""
    signature = [1, 1, 1]
    assert tribonacci(signature, 5) == [1, 1, 1, 3, 5]


def test_zero():
    """Test the result when n is zero."""
    signature = [1, 1, 1]
    assert tribonacci(signature, 0) == []
