"""Reverse a singly linked list."""


class Node:
    """Node is constructed."""

    def __init__(self, val):
        """Val is passed to create an instance of node."""
        self.val = val
        self.next = None


class LinkedList:
    """Linked List construction."""

    def __init__(self):
        """Instance of linked list is created."""
        self.head = None
        self.length = 0

    def push(self, val):
        """Insert a new node at the beginning."""
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def reverse_iterative(self):
        """Reverse a singly linked list in an iterative way."""
        """O(n) / O(1) solution."""
        pre = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = pre
            pre = current
            current = next
        self.head = pre

    def reverse_recur(self):
        """O(n) / O(1)."""
        def _reverse_helper(current, pre):
            """Recursive helper function."""
            if current is None:
                return pre
            next = current.next
            current.next = pre
            pre = current
            current = next
            return _reverse_helper(current, pre)
        self.head = _reverse_helper(current=self.head, pre=None)
