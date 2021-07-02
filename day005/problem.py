def remove_vowels(s):
    """Remove the vowels in the string"""
    new_s = ""
    for char in s:
        if char not in "aeiou":
            new_s += char
    
    return new_s

    