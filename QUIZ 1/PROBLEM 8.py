#####################################################################
#Function for testing the code
#####################################################################


#####################################################################

###PROBLEM 8-1

def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float

    returns the best guess when that guess is less than epsilon
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    for i in range(100):
        # if f(guess) - guess < epsilon:
        # if we don't include the abs, it can be an infinite result or an error.
        if abs(f(guess) - guess) < epsilon:
            return guess
        else:
            guess = f(guess)
    return guess


###PROBLEM 8-2
def sqrt(a):
    def tryit(x):
        return 0.5 * (a/x + x)
    # return fixedPoint(tryit(a), 0.0001)
    # when we call fixedPoint we have to pass a function not a value of a function
    return fixedPoint(tryit, 0.0001)


###PROBLEM 8-3
def babylon(a):
    def test(x):
        return 0.5 * ((a / x) + x)
    return test

def sqrt(a):
    # return fixedPoint(babylon, 0.0001)
    # when returning babylon(a) we can see that returns a FUNCTION, that is test
    # this function returned "test" doesn't have arguments, it is the definition
    # of a function.
    # but when we pass to babylon it asks for an argument!!!
    return fixedPoint(babylon(a), 0.0001)




#############################################################################
##                                MY TESTS
#############################################################################

