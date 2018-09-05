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


def other_reverse_invert(lst):
    """Best practice solution from codewars."""
    from math import copysign as sign
    return [-int(sign(int(str(abs(x))[::-1]), x)) for x in lst
            if isinstance(x, int)]
