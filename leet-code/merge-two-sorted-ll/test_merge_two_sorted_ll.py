"""Test cases."""
from merge_two_sorted_ll import LinkedList, iterative_merge, merge_two_lists
import pytest


@pytest.fixture
def ll_one():
    l1 = LinkedList(1)
    l1.next = LinkedList(2)
    l1.next.next = LinkedList(4)
    return l1

@pytest.fixture
def ll_two():
    l2 = LinkedList(1)
    l2.next = LinkedList(3)
    l2.next.next = LinkedList(4)
    return l2


def test_merge(ll_one, ll_two):
    result = iterative_merge(ll_one, ll_two)
    assert result.val == 1
    assert result.next.val == 1
    assert result.next.next.val == 2
    assert result.next.next.next.val == 3


def test_recur(ll_one, ll_two):
    result = merge_two_lists(ll_one, ll_two)
    assert result.val == 1
    assert result.next.val == 1
    assert result.next.next.val == 2
    assert result.next.next.next.val == 3
