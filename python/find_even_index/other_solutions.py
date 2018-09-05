"""Other user's solutions can be found below."""


def find_even_index_using_built_in(arr):
    """."""
    # this solution does not return 0 for empty array
    # But it is a good reference for using list slicing
    for i in range(len(arr)):
        if sum(arr[i:]) == sum(arr[:i+1]):
            return i
    return -1
