def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a == b:
        return a
    elif a < b:
        divisor = a
        while b%divisor != 0 or a%divisor != 0:
            divisor -= 1
        return divisor
    else:
        divisor = b
        while b%divisor != 0 or a%divisor != 0:
            divisor -= 1
        return divisor
