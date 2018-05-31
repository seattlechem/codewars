"""Test case for find_even_index function."""
from .find_even_index import find_even_index


def test_empty_array():
    """Empty array should return 0."""
    arr = []
    result = find_even_index(arr)
    assert result == 0
