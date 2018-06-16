"""Test cases."""
from sorted_ll_to_bst import LinkedList, convert_ll_bst


head = LinkedList(1)
head.next = LinkedList(2)
head.next.next = LinkedList(3)


def test_true():
    """."""
    res = convert_ll_bst(head)
    assert res.val == 1
