"""Other solutions are added as reference."""


# def solve(n):
#     """Best practicing solution."""
#     a, b = "0", "01"
#     for i in range(0, n):
#         a = b + a
#         a, b = b, a
#     return a
#     pass


def solve(n):
    """Clever solution."""
    # return "0" if n == 0 else "01" if n == 1 else solve(n-1) + solve(n-2)

    if n == 0:
        return '0'
    elif n == 1:
        return '01'
    else:
        return solve(n - 1) + solve(n - 2)
