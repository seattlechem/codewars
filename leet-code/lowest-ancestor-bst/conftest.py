"""Create test TreeNodes."""
import pytest
from lca_bst import TreeNode


@pytest.fixture
def first_bst():
    """First binary search tree."""
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    return root
