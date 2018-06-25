"""Test cases."""
from reverse_ll import LinkedList
import pytest


@pytest.fixture
def simple_ll():
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
    # import pdb; pdb.set_trace()
    simple_ll.reverse_iterative()
    assert simple_ll.head.val == 20
