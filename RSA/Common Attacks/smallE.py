# -*- coding: utf-8 -*-

# Useful when e is small
# Explaination with a small example :
# Let p, q = 19, 23
# e = 3
# N = p * q = 19 * 23 = 437
# pt = 7
# ct = (pt ** e) % N = (7 ** 3) % 437 = 343 (As 343 < 437)
# Even if d can't be calculated, eth root of ct is the plaintext.
# pt = root(ct, e) = root(343, 3) = 7
# The exploit won't work for larger pt, like 10 (As 10 ** 3 > 343 or in general pt ** e > N).
# pt = 10
# ct = (10 ** 3) % 343 = 1000 % 343 = 314
# Won't work!'

from factordb.factordb import FactorDB
from Crypto.Util.number import long_to_bytes
n = int(input("n : "))
e = int(input("e : "))
f = FactorDB(n)
f.connect()
factors = f.get_factor_list()
d1 = {}
for i in factors:
    if i in d1:
        d1[i] += 1
    else:
        d1[i] = 1
shit = 1
for i in d1:
    shit *= i ** (d1[i] // e)
print(long_to_bytes(shit))