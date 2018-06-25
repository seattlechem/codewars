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

    def push(self, val):
        """Insert a new node at the beginning."""
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def reverse_iterative(self):
        """Reverse a singly linked list in an iterative way."""
        """O(n) / O(1) solution."""
        # import pdb; pdb.set_trace()
        pre = None
        current = self.head

        while current is not None:
            next = current.next
            current.next = pre
            prev = current
            current = next
        self.head = prev
