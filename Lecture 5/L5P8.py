def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0:
        return False
    if len(aStr) == 1:
        if char == aStr[0]:
            return True
        else:
            return False
    high = len(aStr)
    low = 0
    middle = int((high+low)/2)
    if middle == 0:
        return False
    elif aStr[middle] == char:
        return True
    elif aStr[middle] > char:
        return isIn(char, aStr[low:middle])
    else:
        return isIn(char, aStr[middle+1:high])