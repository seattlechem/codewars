"""Append the sum of prior 3 elements into original 3 element list."""


def tribonacci(signature, n):
    """Render iterative solutions."""
    res = signature[:n]
    for i in range(n - 3):
        res.append(sum(res[-3:]))
    return res


"""
[:n], from start to n - 1.
In case n = 0, returns []
range(n - 3) ensure n should be greater than 3

"""
