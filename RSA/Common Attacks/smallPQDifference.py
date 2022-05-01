# -*- coding: utf-8 -*-

# Source : https://github.com/Bananacoder404/Prime-factorisation-Fermat
# Theory : https://wiremask.eu/articles/fermats-prime-numbers-factorization/#:~:text=Fermat's%20factorization%20method%20uses%20that,prime%20numbers%20p%20and%20q.
# Fermat's Factorisation
# Useful when p and q differ by a small value.

import numpy, gmpy2
factors = []

n=int(input("n : "))
if n%2==0:
    factors.append(2)
    factors.append(int(n/2))

else:
    x=int(gmpy2.iroot(n, 2)[0]) + 1
    while True:
        y=int(gmpy2.iroot(numpy.power(x, 2)-n, 2)[0])
        yf=int(y)
        if (yf*yf==numpy.power(x, 2)-n):
            factors.append(int(x+y))
            factors.append(int(x-y))
            break
        else:
            x=x+1

print("Factors: " + str(factors))