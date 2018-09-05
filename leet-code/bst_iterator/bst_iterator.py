"""BST iterator."""


class TreeNode():
    """Node class definition."""

    def __init__(self, val):
        """Instance of TreeNode object."""
        self.val = val
        self.left = None
        self.right = None


class BST_Iterator():
    """BST_Iterator class definition."""

    def __init__(self, root):
        """Instance of BST_Iterator object."""
        self.root = root
        self.stack = []

    def hasNext(self):
        """
        :output: boolean value.

        Bool value is returned based on the presence of
        of next smallest number.
        """
        return bool(self.stack or self.root)

    def next(self):
        """Next smallest value."""
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        node = self.stack.pop()
        self.root = node
        self.root = self.root.right
        return node.val
