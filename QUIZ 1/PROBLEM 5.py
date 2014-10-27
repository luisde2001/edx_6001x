def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    """
    # Your Code Here
    sRes =''
    i = 0
    # S1 and S2 equal length
    if len(s1) == len(s2):
        if len(s1) == 0:
            return sRes
        else:
            for i in range (len(s1)):
                sRes = sRes + s1[i]+s2[i]
            return sRes

    # S1 longer than S2
    elif len(s1) > len(s2):
        if len(s2) == 0:
            sRes = s1
        else:
            for i in range (len(s2)):
                sRes = sRes + s1[i] + s2[i]
            sRes = sRes + s1[i+1:]
        return sRes

    # S1 longer than S2
    elif len(s2) > len(s1):
        if len(s1) == 0:
            sRes = s2
        else:
            for i in range (len(s1)):
                sRes = sRes + s1[i] + s2[i]
            sRes = sRes + s2[i+1:]
        return sRes


#############################################################################
##                                MY TESTS
#############################################################################

print laceStrings('', '')
print laceStrings('', 'abc')
print laceStrings('abc', '')
print laceStrings('abc', 'def')
print laceStrings('abc', 'defgh')
print laceStrings('abcd', 'ef')
