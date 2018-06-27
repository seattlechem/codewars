"""Reverse a linked list from m to n positions only."""


class Node:
    """Node class definition."""

    def __init__(self, val=None):
        """Instance of Node class."""
        self.val = val
        self.next = None


class LinkedList:
    """LinkedList class definition."""

    def __init__(self, val=None):
        """Instance of LinkedList class."""
        self.head = Node(val)

    def push(self, val):
        """Insert a node at the beginning."""
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        """Print value of nodes in linked list as array."""
        re = []
        current = self.head
        while current is not None:
            current = self.head
            re.append(current.val)
            current = current.next
        return re


def reverse_between(ll, m, n):
    """Reverse linked list from position m to n."""
    head = ll.head

    if head is None or m == n:
        return ll

    p = dummy = Node()
    dummy.next = head

    for i in range(m - 1):
        p = p.next
        tail = p.next

    for i in range(n - m):
        tmp = p.next
        p.next = tail.next
        tail.next = tail.next.next
        p.next.next = tmp

    return dummy.next
