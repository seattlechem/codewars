"""Find the lowest common ancestor of two given nodes in BST."""


class TreeNode:
    """TreeNode is defined."""

    def __init__(self, val):
        """Val is passed to create a TreeNode."""
        self.val = val
        self.left = None
        self.right = None


def lca_bst_recursive(root, p, q):
    """Lowest common ancestor of two given nodes in BST."""
    if root.val > max(p.val, q.val):
        return lca_bst(root.left, p, q)

    elif root.val < min(p.val, q.val):
        return lca_bst(root.right, p, q)

    else:
        return root



def lowestCommonAncestor(root, p, q):
    """O(n) solution."""
    while root:
        if p.val < root.val > q.val:
            # p and q smaller, mean they locate left
            root = root.left
        elif p.val > root.val < q.val:
            root = root.right
        else:
            # otherwise the lowest common ancestor is root
            return root


def lca_three_lines(root, p, q):
    while (root.val - p.val) * (root.val - q.val) > 0:
        #this means either both p and q are smaller or greater than root
        root = (root.left, root.right)[p.val > root.val]
        # it could be q.val, but in this case p was chosen
        # if p is greater than root.val (either True (1) False(0))
        # root.left or root.right is chosen depends on index (1 or 0)
    return root
