def longestCommonPrefix(strs):
    #Declare placement in the list of strings
    #Use the last item in string as a starter for prefixes 
    
    #While placement is in range of list of strings
        # Check if compare is not in item in list indexed by placement
            #Then slice the string and move on
        # If the compare is in the string of placement 
            # move onto the next item in list 
    
    #After that, get compare
    compare = strs.pop()   #"flight"
    
    while len(strs)!=0:
        if compare not in strs[0] or compare not in strs[0][:len(compare)]:
            compare = compare[:-1]
        else:
            strs.pop(0)
    return compare 

longestCommonPrefix(["reflower","flow","flight"])

def isPalindrome(x):
    if x < 0 or (x%10 == 0 and x!=0):
        return False
    reversed_x = 0
    while  x > reversed_x:
        reversed_x = (reversed_x * 10 + (x%10))
        x = x//10
    if x==reversed_x or x==reversed_x//10:
        return True
    return False