"""Return two indices from array where two add up to target."""


def two_sum(arr, target):
    """
    Values.

    :input: array and target value
    :output: array (containing two indices)
    :Time: O(n2)
    :Space: O(1)
    """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]


def two_sum_dict(arr, target):
    """
    Increase speed by using dictionary.

    :Time: O(n)
    :Space: O(n)
    """
    re = {}
    for i in range(len(arr)):
        re[arr[i]] = i

    for i in range(len(arr)):
        diff = target - arr[i]
        if diff in re:
            return [i, re[diff]]
