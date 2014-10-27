def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    myResult = 1
    y = 0
    while myResult <= x:
        myResult= myResult*b
        y = y+1
    return (y-1)

#############################################################################
##                                MY TESTS
#############################################################################

print myLog(27, 3)
print myLog(26, 3)
print myLog(28, 3)
print myLog(4, 16)
print myLog(20, 12)
print myLog(25, 3)
print myLog(124, 2)
print myLog(168, 7)
