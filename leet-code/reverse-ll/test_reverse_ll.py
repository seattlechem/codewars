"""Test cases."""
from reverse_ll import LinkedList
import pytest


@pytest.fixture
def simple_ll():
    """Create a simple linked list."""
    ll = LinkedList()
    ll.push(20)
    ll.push(4)
    ll.push(15)
    ll.push(85)
    return ll


def test_true(simple_ll):
    """True test case."""
    assert simple_ll.head.val == 85
    assert isinstance(simple_ll, LinkedList) is True
    simple_ll.reverse_iterative()
    assert simple_ll.head.val == 20
    assert simple_ll.length == 4
    assert simple_ll.head.next.val == 4
    assert isinstance(simple_ll, LinkedList) is True
    simple_ll.reverse_recur()
    assert isinstance(simple_ll, LinkedList) is True
    assert simple_ll.head.val == 85
    assert simple_ll.head.next.val == 15
    assert simple_ll.head.next.next.val == 4
