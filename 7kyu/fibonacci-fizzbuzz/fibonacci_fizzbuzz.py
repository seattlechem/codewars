"""Fibonacci fizz buzz."""


def fibs_fizz_buzz(k):
    """My fibonacci fizz buzz solution."""
    res = [1, 1]
    # n has to be greater than 2
    if k <= 2:
        return res[:k]
    else:
        for i in range(k - 2):
            res.append(res[i] + res[i + 1])

        for i in range(len(res)):
            # always and condition must be checked first
            if res[i] % 15 == 0:
                res[i] = 'FizzBuzz'
            elif res[i] % 5 == 0:
                res[i] = 'Buzz'
            elif res[i] % 3 == 0:
                res[i] = 'Fizz'
        return res
