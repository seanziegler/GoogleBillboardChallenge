import math

def basicPrime(n):
    if n <= 2:
        raise ValueError
    if not type(n) == int:
        raise TypeError   
    prime = True
    for iter in range(2, math.floor(math.ceil(math.sqrt(n))) + 1):
        if n % iter == 0:
            prime = False
            break
    if prime:
        print('%s is the first 10 digit prime in e.' % n)
    return prime
