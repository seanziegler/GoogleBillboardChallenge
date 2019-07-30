import math
from fractions import gcd

def fermatPrime(n):
    tests = [1,5,7,12,33,54] # make random less than n
    prime = True
    for a in tests:
        x = gcd(a,n) == 1 # why
        y = (int(math.pow(a, n)) -1) % n == 1
        print('n: %s A: %s GCD: %s Fermat: %s' % (n, a, x, y))
        if not x or not y:
            prime = False
            break
    if prime:
        print('%s is a prime number' % n)

    return prime
