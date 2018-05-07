"""Add two numbers code challenge."""


class ListNode:
    """ListNode object definition."""

    def __init__(self, x):
        """Instance of ListNode object."""
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """Add two values of linked lists and return a new linked list."""
    x1 = ''
    x2 = ''

    current = l1
    while current:
        x1 += str(current.val)
        current = current.next

    current = l2
    while current:
        x2 += str(current.val)
        current = current.next

    x1 = x1[::-1]
    x2 = x2[::-1]

    y = int(x1) + int(x2)
    y = str(y)
    y = y[::-1]

    head = result = ListNode(y[0])
    for i in range(1, len(y)):
        result.next = ListNode(y[i])
        result = result.next
    return head
