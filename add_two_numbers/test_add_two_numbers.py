"""Add two number test cases."""

import pytest
from .add_two_numbers import ListNode
from .add_two_numbers import addTwoNumbers


@pytest.fixture
def l1():
    """Three node linked list."""
    head = l1 = ListNode(3)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    return head


@pytest.fixture
def l2():
    """Another three node linked list."""
    head = l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(5)
    return head


def test_addition(l1, l2):
    """Confirm the result of addition of two linked list."""
    result = addTwoNumbers(l1, l2)
    assert result.val == '5'
    assert result.next.val == '8'
    assert result.next.next.val == '0'
    assert result.next.next.next.val == '1'
