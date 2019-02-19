import math
import timeit
from decimal import *
from checkPrime import *

tic = timeit.default_timer()

# Set higher precision than python's default
getcontext().prec = 1000

e = Decimal(1).exp()
e = str(e).replace('.','') # Remove decimal from string

prime = False
index = 0
while prime == False:
    prime = checkPrime(int(e[index:index+10]))
    if prime == True:
        print('Prime found! %s' % e[index:index+10])
        break
    else:
        index += 1

toc = timeit.default_timer()
print(toc - tic)
