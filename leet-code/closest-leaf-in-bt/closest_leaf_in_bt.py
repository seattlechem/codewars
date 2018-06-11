"""."""


def find_closest_leaf(root, k):
    """Find closest leaf of a given value in binary tree."""
    """
    :input: root and int k
    :output: int
    """
    # neighbors dictionary
    neighbors = {}
    # leaves: list, store leaf int values
    leaves = []

    def traverse(node, neighbors, leaves):
        """Traverse binary tree to find the leaves."""
        # if node is not True, if node is None?
        if not node:
            return
        # node left and right do not exist, which means it is a leaf
        if not node.left and not node.right:
            leaves.add(node.val)
        if node.left:
            # if left exists, add node and node.left relationship into
            # neighbors as dict
            neighbors[node.val].append(node.left.val)
            neighbors[node.left.val].append(node.val)
            traverse(node.left, neighbors, leaves)
        if node.right:
            neighbors[node.val].append(node.right.val)
            neighbors[node.right.val].append(node.val)
            traverse(node.right, neighbors, leaves)


