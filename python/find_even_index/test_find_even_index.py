"""Test case for find_even_index function."""
from find_even_index import find_even_index


def test_empty_array():
    arr = []
    result = find_even_index(arr)
    assert result == 0
