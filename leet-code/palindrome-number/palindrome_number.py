"""Determine if number is palindrome."""


def isPalindrome(x):
    """
    Take integer number and determine if palindrome.

    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    # convert to string
    x = str(x)
    if x[-1] == '0' and len(x) > 1:
        return False

    if x == x[::-1]:
        return True
    return False
