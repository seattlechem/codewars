"""Test cases."""
from minimum_depth_bt import min_depth, Node


root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

root_zero = Node()


def test_true():
    """Assert if returns correct min depth."""
    assert min_depth(root) == 2
