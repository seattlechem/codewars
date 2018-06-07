"""Simple fibonacci strings."""


def simple_fibonacci_strings(k):
    """Strings are concatenated backward."""
    res = ['0', '01']

    if k > 1:
        for i in range(k - 1):
            # k does not change. i is the one will change.
            res.append(res[i + 1] + res[i])

        # join elements in list
        return res[k]

    else:
        return res[k]
