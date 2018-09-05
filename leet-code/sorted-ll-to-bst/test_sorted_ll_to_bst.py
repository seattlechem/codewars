"""Test cases."""
from sorted_ll_to_bst import LinkedList, Convert
import pytest


@pytest.fixture
def simply_ll():
    """."""
    heady = LinkedList(1)
    heady.next = LinkedList(2)
    heady.next.next = LinkedList(3)
    return heady


def test_true(simply_ll):
    """."""
    res = Convert().sorted_list_to_bst(simply_ll)
    assert res.val == 2
    assert res.left.val == 1
    assert res.right.val == 3
