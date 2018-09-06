"""Longest substring in string."""


def lengthOfLongestSubstring(s):
    """Longest substring is returned as its string length in numeric."""
    dict, res, start = {}, 0, 0

    for i in range(len(s)):
        if s[i] in dict:
            res = max(res, i - start)
            start = max(start, dict[s[i]] + 1)
        dict[s[i]] = i
    return max(res, len(s) - start)
