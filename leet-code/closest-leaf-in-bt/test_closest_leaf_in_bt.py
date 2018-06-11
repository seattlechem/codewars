"""Test cases."""
from closest_leaf_in_bt import Node
from closest_leaf_in_bt import find_closest_leaf


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(5)
root.left.left.left.left = Node(6)


def test_find_k_2():
    """."""
    assert find_closest_leaf(root, 2) == 3
