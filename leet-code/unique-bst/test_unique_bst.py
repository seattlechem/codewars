"""Test cases."""
from unique_bst import numTrees


def test_true():
    """."""
    assert numTrees(3) == 5
    assert numTrees(4) == 14
