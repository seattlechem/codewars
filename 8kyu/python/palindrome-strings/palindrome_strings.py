"""Palindrome strings solution."""


def is_palindrome(line):
    """Return True if it is palindrome string."""
    return str(line) == str(line)[::-1]
