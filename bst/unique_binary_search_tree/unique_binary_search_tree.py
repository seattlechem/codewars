"""Unique Binary Search Tree."""


def num_trees(n):
    """Specify how many structurally unique BST that store values 1..n."""
    dp = [1 for _ in range(n + 1)]
    # import pdb; pdb.set_trace()
    for i in range(2, n + 1):
        s = 0
        for j in range(i):
            s += dp[j] * dp[i - j - 1]
        dp[i] = s
    return dp[-1]
