"""Test cases."""
from verify_preorder_bt import Node, verify_preorder


root = Node(40)
root.left = Node(30)
root.right = Node(80)
root.right.right = Node(100)
root.left.left = Node(35)


def test_true():
    """True test case."""
    assert verify_preorder(root, [40, 30, 35, 80, 100]) is True
