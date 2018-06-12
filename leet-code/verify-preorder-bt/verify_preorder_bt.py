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


def verify_preorder_o1(preorder):
    """Verify if given array is a preorder traversal of binary tree."""
    low, i = float('-inf'), -1
    import pdb; pdb.set_trace()
    for k in preorder:
        if k < low:
            return False
        while i >= 0 and k > preorder[i]:
            low = preorder[i]
            i -= 1
        i += 1
        preorder[i] = k
    return True
