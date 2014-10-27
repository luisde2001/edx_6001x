#-------------------------------------------------------------------------------
# Name:        RADIATION EXPOSURE
# Purpose:
#
# Author:      lmdefrancisco
#
# Created:     11/09/2014
# Copyright:   (c) lmdefrancisco 2014
# Licence:     GPL
#-------------------------------------------------------------------------------

def f(x):
    import math
    return 200*math.e**(math.log(0.5)/14.1 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...

    radiation = 0
    i = start
    #for i in range(start, stop, step):
    while i < stop:
        radiation += step*f(i)
        print (i, f(i), radiation)
        i += step

    return radiation

print (radiationExposure(0, 3, 0.1))