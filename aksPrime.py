import math
from fractions import gcd

def fermatPrime(n):
    prime = True
    a_tests = [1,5,7,12,33,54]
    for a in a_tests:
        x = gcd(a,n)
        y = int(math.pow(a, n-1)) % n == 1
        print('A: %d GCD: %d Math: %d' % (a, x, y))
        if gcd(a,n) == 1 & int(math.pow(a, n-1)) % n == 1:
            continue
        else:
            prime = False
            print('%d is not prime' % n)
            break
    if prime == True:
        print('%d is prime' % n)

if __name__== "__main__":
    n = input('Enter a number to test for primality: ')
    fermatPrime(int(n))
