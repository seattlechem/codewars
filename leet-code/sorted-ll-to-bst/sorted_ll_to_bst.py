"""Convert a sorted linked list to binary search tree."""


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


def convert_ll_bst(head):
    """Convert linked list to bst."""
    def sorted_list_to_bst(head):
        """Figure out length of ll."""
        current, length = head, 0
        import pdb; pdb.set_trace()
        while current is not None:
            current, length = current.next, length + 1
        return sorted_list_to_bst_recur(0, length)

    def sorted_list_to_bst_recur(start, end):
        """Convert a ll to bst."""
        if start == end:
            return None
        mid = start + end - start / 2
        left = sorted_list_to_bst_recur(start, mid)
        current = TreeNode(head.val)
        current.left = left
        head = head.next
        current.right = sorted_list_to_bst_recur(mid + 1, end)
        return current
