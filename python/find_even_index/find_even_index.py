"""Codewars problem to find even index."""


def find_even_index(arr):
    """Return the index where sum of both sides are equal."""
    for i in range(0, len(arr)):
        sum1 = 0
        sum2 = 0

        for j in range(0, i):
            sum1 += arr[j]
        for k in range(i + 1, len(arr)):
            sum2 += arr[k]
        if sum1 == sum2:
            return i
    return -1
