def genPrimes():
    '''
    Genarates prime numbers in a list
    '''
    primes = []
    number = 1
    flag = True
    while True:
        number += 1
        for p in primes:
            if number%p == 0:
                flag = False
                break
            else:
                flag = True

        if flag == True:
            primes.append(number)
            yield number


    print primes

genPrimes()
