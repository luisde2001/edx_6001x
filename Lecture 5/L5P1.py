#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Name:        PS2.3 PAYING DEBT OFF IN A YEAR BISECTION
# Purpose:
#
# Author:      lmdefrancisco
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    for i in range (0,exp):
        result = result * base
    return result

