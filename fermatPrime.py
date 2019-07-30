import math
import random
from fractions import gcd

def fermatPrime(n):
    tests = [random.randint(2,10) for i in range(5)]
    prime = True

    for a in tests:
        print(a,n)
        x = gcd(a,n) == 1 # why
        y = (a**n - 1) % n == 1
        print('n: %s A: %s GCD: %s Fermat: %s' % (n, a, x, y))
        if not x or not y:
            prime = False
            break
    if prime:
        print('%s is the first 10 digit prime in e.' % n)

    return prime
