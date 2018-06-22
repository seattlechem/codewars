"""Test cases."""
from lca_bst import lca_bst


class Node:
    """Node class declared."""

    def __init__(self, val):
        """Instance of Node class."""
        self.val = val


def test_true(first_bst):
    """Test true."""
    result = lca_bst(first_bst, Node(2), Node(8))
    assert result.val == 6
    assert lca_bst(first_bst, Node(2), Node(4)).val == 2
