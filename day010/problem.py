def firstNotRepeatingCharacter(s):
    """Return the first instance in the given string"""
    dic = {}
    
    for char in s:
        if char not in dic:
            dic[char] = 0
        
        dic[char] += 1
        
    for letter in s:
        if dic[letter] == 1:
            return letter
    
    return '_'