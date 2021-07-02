#Two sum
def two_sum(num, target):
    """Return the list of the indexes of the num that add to the target"""
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target-num], i]
        d[num] = i

