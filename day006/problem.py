def running_sum(num):
    """Return the running sum of nums"""
    for i in range(1, len(num)):
        num[i] += num[i-1]

    return num
    