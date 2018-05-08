"""Unique binary search tree test cases."""
from .unique_binary_search_tree import num_trees
import pytest


def test_simple_n_3():
    """In case n = 3."""
    assert num_trees(3) == ''
