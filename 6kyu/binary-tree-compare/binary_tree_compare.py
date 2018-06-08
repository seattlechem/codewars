"""Compare if two binary trees are identical."""


def compare(a, b):
    """Compare two binary trees to determine if they are identical."""
    if a is None and b is None:
        return True
    if a is not None and b is not None:
        return (a.val == b.val) and compare(a.left, b.left)\
                                and compare(a.right, b.right)
    return False
