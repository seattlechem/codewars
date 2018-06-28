"""Return two indices from array where two add up to target."""


def two_sum(arr, target):
    """
    Values.

    :input: array and target value
    :output: array (containing two indices)
    :Time: O(n)
    :Space: O(1)
    """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
