"""Test cases."""
from reverse_ll_2 import LinkedList, reverse_between
import pytest


@pytest.fixture
def simple_ll():
    """Linked list for test."""
    ll = LinkedList(6)
    ll.push(5)
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(1)
    return ll


def test_true(simple_ll):
    """Compare return linked list."""
    re = reverse_between(simple_ll, 2, 5)
    assert re.val == 1
    assert re.next.val == 5
    assert re.next.next.val == 4
    assert re.next.next.next.val == 3
    assert re.next.next.next.next.val == 2
    assert re.next.next.next.next.next.val == 6
    assert re.next.next.next.next.next.next is None
