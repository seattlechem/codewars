"""Convert a sorted linked list to binary search tree."""
import math


class TreeNode:
    """Tree Node class."""

    def __init__(self, val):
        """."""
        self.val = val
        self.left = None
        self.right = None


class LinkedList:
    """Linked list class."""

    def __init__(self, val):
        """."""
        self.val = val
        self.next = None


class Convert:
    """Convert linked list to bst."""

    head = None

    def sorted_list_to_bst(self, head):
        """Figure out length of ll."""
        current, length = head, 0
        # import pdb; pdb.set_trace()
        while current is not None:
            current, length = current.next, length + 1
        self.head = head
        return self.sorted_list_to_bst_recur(0, length)

    def sorted_list_to_bst_recur(self, start, end):
        """Convert a ll to bst."""
        # import pdb; pdb.set_trace()
        if start == end:
            return None
        mid = math.floor(start + (end - start) / 2)
        left = self.sorted_list_to_bst_recur(start, mid)
        current = TreeNode(self.head.val)
        current.left = left
        self.head = self.head.next
        current.right = self.sorted_list_to_bst_recur(mid + 1, end)
        return current
