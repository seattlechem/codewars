"""Find the lowest common ancestor of two given nodes in BST."""


class TreeNode:
    """TreeNode is defined."""

    def __init__(self, val):
        """Val is passed to create a TreeNode."""
        self.val = val
        self.left = None
        self.right = None


def lca_bst(root, p, q):
    """Lowest common ancestor of two given nodes in BST."""
    if root.val > max(p.val, q.val):
        return lca_bst(root.left, p, q)

    elif root.val < min(p.val, q.val):
        return lca_bst(root.right, p, q)

    else:
        return root
