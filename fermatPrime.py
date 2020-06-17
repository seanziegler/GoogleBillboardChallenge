import math
import random

def fermatPrime(n):
    if n <= 2:
        raise ValueError
    if not type(n) == int:
        raise TypeError
    tests = [2, 4, 6, 8, 9]
    prime = True

    for a in tests:

        x = math.gcd(a, n) == 1  # why
        y = pow(a, n-1, n) == 1
        if not x or not y:
            prime = False
            break
        print(a, n, prime)
    if prime:
        print('%s is the first 10 digit prime in e.' % n)

    return prime
