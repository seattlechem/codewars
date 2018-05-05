"""Add two numbers code challenge."""


class ListNode:
    """ListNode object definition."""

    def __init__(self, x):
        """Instance of ListNode object."""
        self.val = x
        self.next = None


def addTwoNumbers(self, l1, l2):
    """Add two values of linked lists and return a new linked list."""
    current = l1.head
    current2 = l2.head
    l3 = ListNode(0)
    result = l3.head

    while current and current2:
        result.val = current.val + current2.val

        current = current.next
        current2 = current2.next
        result = result.next
    
    return result
