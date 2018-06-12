"""When given value k, it returns the closest leaf and its distance."""
import collections


class Node:
    """Node class definition."""

    def __init__(self, val):
        """Definition for constructor."""
        self.val = val
        self.left = None
        self.right = None


def find_closest(root, k):
    """Input root and given k, output closest leaf and its distance in int."""
    neighbors = collections.defaultdict(list)
    leaves = set()

    def traverse(node, neighbors, leaves):
        if not node:
            return
        if not node.left and not node.right:
            leaves.add(node.val)
        if node.left:
            neighbors[node.val].append(node.left.val)
            neighbors[node.left.val].append(node.val)
            traverse(node.left, neighbors, leaves)
        if node.right:
            neighbors[node.val].append(node.right.val)
            neighbors[node.right.val].append(node.val)
            traverse(node.right, neighbors, leaves)

    traverse(root, neighbors, leaves)

    qu, lookup = [k], set([k])
    dst = 0
    result = {'val': [], 'dist': []}

    while qu:
        qu_next = []
        for uu in qu:
            if uu in leaves:
                result['val'].append(uu)
                result['dist'].append(dst)
            for v in neighbors[uu]:
                if v in lookup:
                    continue
                lookup.add(v)
                qu_next.append(v)
        if len(result['val']) > 0:
            return result
        qu = qu_next
        dst += 1
    return 0
