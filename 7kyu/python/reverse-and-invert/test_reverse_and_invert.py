"""Test cases."""
from reverse_and_invert import reverse_invert


def test_true():
    """True test cases."""
    assert reverse_invert([1, 2, 3, 4, 5]) == [-1, -2, -3, -4, -5]
    assert reverse_invert([-10]) == [1]
    assert reverse_invert([- 9, - 18, 99]) == [9, 81, - 99]
    assert reverse_invert([1, 12, 'a', 3.4, 87, 99.9, -42,
                           50, 5.6]) == [- 1, -21, -78, 24, -5]
    assert reverse_invert([]) == []
