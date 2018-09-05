"""Recursive and Iterative solutions."""


class LinkedList:
    """Linked List class."""

    def __init__(self, val):
        """Create a linked list."""
        self.val = val
        self.next = None


def iterative_merge(l1, l2):
    """Solved in an iterative way."""
    prehead = LinkedList(-1)
    pre = prehead

    while l1 and l2:
        if l1.val <= l2.val:
            pre.next = l1
            l1 = l1.next

        else:
            pre.next = l2
            l2 = l2.next

        pre = pre.next
    pre.next = l1 if l1 is not None else l2

    return prehead.next


def merge_two_lists(l1, l2):
    """Solved in a recursive way."""
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2
