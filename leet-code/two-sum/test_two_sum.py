"""Test cases."""
from two_sum import two_sum, two_sum_dict


def test_true():
    """True case test."""
    assert two_sum([1, 2, 5, 6, 7], 9) == [1, 4]
    assert two_sum_dict([1, 2, 5, 6, 7], 9) == [1, 4]
