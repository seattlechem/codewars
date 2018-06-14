"""Reverse and invert integer."""


def reverse_invert(lst):
    """Reverse only integer and convert its sign."""
    import math
    res = []
    for e in lst:
        if type(e) is int:
            sign = e
            if e < 0:
                e = e * - 1
            res.append(math.copysign(int(str(e)[::-1]), sign * - 1))
    return res
