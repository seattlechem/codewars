"""Simple rotated palindrome solution."""


def solve(st):
    """Return True if a string is palindrome after rotating to left."""
    def is_palindrome(st):
        return str(st) == str(st)[::-1]
    if is_palindrome(st) is True:
        return True
    st_list = list(str(st))
    for i in range(0, len(st_list)):
        last = st_list.pop()
        st_list.insert(0, last)
        st = ''.join(st_list)
        if is_palindrome(st) is True:
            return True
    return False


def best_solve(s):
    """Best practice solution from codewars."""
    return any(s[i+1:] + s[:i+1] == s[i::-1] + s[:i:-1] for i in range(len(s)))
