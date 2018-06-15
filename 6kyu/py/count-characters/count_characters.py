"""Counter characters in a string."""


def count(string):
    """Return dict as a result."""
    # Used defaultdict b/c a regular dict return KeyError during for loop
    # The function code should be here
    from collections import defaultdict
    res = defaultdict(int)
    for i in string:
        res[i] += 1
    return res


def other_count(string):
    """Regular dict is used."""
    r = {}
    for c in string:
        if c in r:
            r[c] += 1
        else:
            r[c] = 1
    return r


def counter_count(string):
    """String's counter() method is used."""
    return {i: string.count(i) for i in string}
