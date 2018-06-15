"""Test cases."""
from count_characters import count


def test_true():
    """True test cases."""
    assert count('aba') == {'a': 2, 'b': 1}
    assert count('') == {}
