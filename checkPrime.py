import math

def checkPrime(n):
    prime = True
    for iter in range(2, math.floor(math.sqrt(n) + 1)):
        if n % iter == 0:
            prime = False
            break
    if prime == True:
        print('%d is a prime number' % n)
    return prime

if __name__== "__main__":
    n = input('Enter a number to test for primality: ')
    checkPrime(int(n))
