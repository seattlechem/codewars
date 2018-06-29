"""Find three elements from array where their sum equals to zero."""


def three_sum(nums):
    """
    Take array and find 3 elements where their sum equals to zero.

    :input: List[int]
    :output: List[List[int]]
    """
    # check if there's at least three elements
    # import pdb; pdb.set_trace()
    if len(nums) < 3:
        return []

    # sort the input array
    nums.sort()
    # create an instance of set object for return
    s = set()
    re = []

    # iterate input nums using enumerate()
    for k, v in enumerate(nums):
        # define two pointers
        h, r = k + 1, len(nums) - 1

        while h < r:
            sums = v + nums[h] + nums[r]
            # check to see if sums = 0
            if sums == 0:
                if (v, nums[h], nums[r]) not in s:
                    s.add((v, nums[h], nums[r]))
                    re.append([v, nums[h], nums[r]])

                # s.add((v, nums[h], nums[r]))
                # since nums are sorted, if nums[l] and nums[k] are same, no
                # need to iterate any further
                if nums[h] == nums[r]:
                    break

                h += 1
                r -= 1
            elif sums > 0:
                # in this case, just decrease the greatest value
                # in this case, r
                r -= 1

            elif sums < 0:
                # try to tweak the l value while fixing r
                h += 1

    return re
