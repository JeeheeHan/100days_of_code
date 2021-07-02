def firstDuplicate(a):
    """Find the first duplicate in the give list"""
    existing_num = set() 
    duplicate = -1

    for num in a:
        if num not in existing_num:
            existing_num.add(num)
        else:
            duplicate = num
            break

    return duplicate