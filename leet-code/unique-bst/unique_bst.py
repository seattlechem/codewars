"""Number of unique binary trees."""


def numTrees(n):
    """
    O(n^2) / O(n).

    :type n: int
    :rtype: int
    """
    N = {}
    N[0] = 1
    N[1] = 1

    for i in range(2, n + 1):
        N[i] = 0
        for j in range(0, i):
            N[i] += N[j] * N[i - j - 1]

    return N[n]
