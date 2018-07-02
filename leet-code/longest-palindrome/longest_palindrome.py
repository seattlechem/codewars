"""Longest palindrome substring."""


def longest_palindrome(s):
    """."""
    n = len(s)
    table = [[]]
    # max_length = 1
    for i in range(n):
        table[i][i] = True

    # max_length = 2
    start = 0
    i = 0
    while i < n - 1:
        if s[i] == s[i + 1]:
            table[i][i + 1] = True
            start = i
            max_length = 2
        i = i + 1

    # max_length > 2
    k = 3
    while k <= n:
        i = 0
        while i < n - k + 1:
            j = i + k - 1
            if s[i + 1][j - 1] and s[i] == s[j]:
                table[i][j] = True

                if k > max_length:
                    start = i
                    max_length = k
            i = i + 1
    k = k + 1

    return s[start:start + max_length - 1]
