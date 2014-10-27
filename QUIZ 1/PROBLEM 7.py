#####################################################################
#Function for testing the code
#####################################################################
def test():
    print 0, McNuggets(0)
    print 5, McNuggets(5)
    print 6, McNuggets(6)
    print 7, McNuggets(7)
    print 8, McNuggets(8)
    print 9, McNuggets(9)
    print 10, McNuggets(10)
    print 12, McNuggets(12)
    print 15, McNuggets(15)
    print 18, McNuggets(18)
    print 19, McNuggets(19)
    print 20, McNuggets(20)
    print 21, McNuggets(21)
    print 26, McNuggets(26)
    print 29, McNuggets(29)
    print 35, McNuggets(35)
    print 40, McNuggets(40)

#####################################################################

def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    a = 0
    b = 0
    c = 0
    result = False

    def resComb(a, b, c):
        return a*6 + b*9 + c*20

    while a < n:
        b = 0

        while b < n:
            c = 0

            while c < n:
                if resComb(a, b, c) == n:
                    return True
                c += 1

            b += 1

        a += 1

    return result











#############################################################################
##                                MY TESTS
#############################################################################

test()