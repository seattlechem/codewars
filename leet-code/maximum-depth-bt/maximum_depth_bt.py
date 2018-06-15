"""Maximum depth of binary tree."""


def max_depth(root):
    """Figure out what is maximum depth of a given binary tree is."""
    if root is None:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1
