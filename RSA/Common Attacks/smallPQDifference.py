# -*- coding: utf-8 -*-

# Source : https://github.com/Bananacoder404/Prime-factorisation-Fermat
# Theory : https://wiremask.eu/articles/fermats-prime-numbers-factorization/#:~:text=Fermat's%20factorization%20method%20uses%20that,prime%20numbers%20p%20and%20q.
# Fermat's Factorisation
# Useful when p and q differ by a small value.
import gmpy2

N = int(input("n : "))
def fermat_factor(n):
    assert n % 2 != 0

    a = gmpy2.isqrt(n)
    b2 = gmpy2.square(a) - n

    while not gmpy2.is_square(b2):
        a += 1
        b2 = gmpy2.square(a) - n

    p = a + gmpy2.isqrt(b2)
    q = a - gmpy2.isqrt(b2)

    return int(p), int(q)

if __name__ == "__main__":
    (p, q) = fermat_factor(N)

    print("p = {}".format(p))
    print("q = {}".format(q))
