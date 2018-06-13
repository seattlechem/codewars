"""Simple rotated palindrome solution."""


def solve(st):
    """Return True if a string is palindrome after rotating to left."""
    def is_palindrome(st):
        return str(st) == str(st)[::-1]
    if is_palindrome(st) is True:
        return True
    st_list = list(str(st))
    for i in range(0, len(st_list) - 1):
        last = st_list.pop()
        st_list.insert(0, last)
        st = ''.join(st_list)
        if is_palindrome(st) is True:
            return True
    return False
