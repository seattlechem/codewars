"""
Verify if a given array is a correct representation of.

preorder of traversal of the corresponding binary tree.
"""


class Node:
    """Node class definitions."""

    def __init__(self, val):
        """Node class is constructed."""
        self.val = val
        self.left = None
        self.right = None


def verify_preorder(root, arr):
    """
    Return True if the array is correct.

    True if the array is correct representation of preorder traversal of
    the given binary tree.
    """
    veri_list = []

    def traverse(node):
        """."""
        if not node:
            return
        if node:
            veri_list.append(node.val)
        if node.left:
            traverse(node.left)
        if node.right:
            traverse(node.right)

        traverse(root)

        if veri_list == arr:
            return True
        return False
