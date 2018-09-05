"""Test cases."""
from three_sum import three_sum


def test_true():
    """."""
    assert three_sum([-4, -1, -1, 0, 1, 2]) == [[-1, -1, 2], [-1, 0, 1]]
