def is_unique(sample):
    # Check if chars in string are unique using sets
    if len(set(sample)) == len(sample):
        return True
    return False

def check_permutation(sample, sample2):
    # check if string is permutation
    if sorted(sample) == sorted(sample2):
        return True 