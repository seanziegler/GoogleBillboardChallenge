# need to write unit tests for both prime algorithms
# check edge cases (int, str, float, zero, negative, first 100 primes, first 100 non primes)

from decimal import *
import timeit
from basicPrime import basicPrime
from fermatPrime import fermatPrime

def main(algo):
    tic = timeit.default_timer()

    #store e to 1000 digits
    getcontext().prec = 1000

    e = Decimal(1).exp()
    e = str(e).replace('.','') #Remove decimal from string

    prime = False
    index = 0

    while prime == False:
        n = int(e[index:index+10])
        if algo == 1:
            prime = basicPrime(n)
        elif algo == 2:
            prime = fermatPrime(n)
        index += 1

    toc = timeit.default_timer()
    print(toc - tic)

if __name__ == "__main__":
    algo = int(input('Let\'s find the first 10 digit prime in e. \nChoose an algorithm: \n(1) Basic Primality \n(2) Fermat Primality\n'))
    main(algo)
