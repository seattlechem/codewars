"""Find minimum depth of binary tree."""


class Node:
    """Node class."""

    def __init__(self, val):
        """Node class is constructed."""
        self.val = val
        self.left = None
        self.right = None


def min_depth(root):
    """Figure out minimum depth of binary tree."""
    if root is None:
        return 0
    if root.left and root.right:
        return min(min_depth(root.left), min_depth(root.right)) + 1
    else:
        return max(min_depth(root.left), min_depth(root.right)) + 1


"""
:time(On)
:space(Oh)
"""
