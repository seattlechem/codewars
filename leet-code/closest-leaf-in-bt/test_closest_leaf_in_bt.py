"""Test cases."""
from closest_leaf_in_bt import Node
from closest_leaf_in_bt import find_closest_leaf


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(None)
root.right.left.left = Node(None)
root.right.left.left.left = Node(None)
root.right.left.left.right = Node(5)
root.right.right.right = Node(None)
root.right.right.right.left = Node(6)


def test_find_k_2(root):
    """."""
    assert find_closest_leaf(root, 2) == 3
