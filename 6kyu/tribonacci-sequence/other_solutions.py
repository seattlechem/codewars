"""Other solutions submitted by codewars users."""


def tribonacci(signature, n):
    """Solution used while statement."""
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    return signature[:n]


def tribonacci_1(s, n):
    """Solution used for loop."""
    # start from i = 3
    # this does not cover when n is less than 3
    for i in range(3, n):
        s.append(s[i-1] + s[i-2] + s[i-3])
    return s[:n]
