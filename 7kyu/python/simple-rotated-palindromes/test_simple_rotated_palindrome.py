"""Test cases."""
from simple_rotated_palindrome import solve


def test_true():
    """Codewars test cases."""
    assert solve("aaab") is False
    assert solve("abcabc") is False
    assert solve("4455") is True
    assert solve("zazcbaabc") is True
    assert solve("223456776543") is True
    assert solve("432612345665") is False
    assert solve("qponmlkjihgfeeiefghijklmnopqrsttsr") is False
