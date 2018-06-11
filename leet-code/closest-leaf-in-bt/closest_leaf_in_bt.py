"""."""
import collections


class Node(object):
    """Node class definition."""

    def __init__(self, x):
        """Node class constructor."""
        self.val = x
        self.left = None
        self.right = None


def find_closest_leaf(root, k):
    """Find closest leaf of a given value in binary tree."""
    """
    :input: root and int k
    :output: int
    """
    # neighbors in defaultdict
    neighbors = collections.defaultdict(list)
    # leaves: list, store leaf int values
    leaves = set()

    def traverse(node, neighbors, leaves):
        """Traverse binary tree to find the leaves."""
        # if node is not True, if node is None?
        # import pdb; pdb.set_trace()
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

    traverse(root, neighbors, leaves)
    qu, lookup = [k], set([k])

    while qu:
        next_qu = []
        for i in qu:
            if i in leaves:
                return i
            for v in neighbors[i]:
                if v in lookup:
                    continue
                lookup.add(v)
                next_qu.append(v)
        qu = next_qu
    return 0
