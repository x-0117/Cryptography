# -*- coding: utf-8 -*-
from factordb.factordb import FactorDB
from Crypto.Util.number import long_to_bytes

l1 = open('C:/Users/User/H4ck_54w/Crypto_/vishwaJumbleBumble/JumbleBumble.txt', 'r').read().split('\n\n')
l2 = []
for i in l1:
    try:
        l2.append(int(i.split('\n')[2]))
    except:
        pass

for i in l2:
    f = FactorDB(i)
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
        shit *= i ** (d1[i] // 4)
    print(long_to_bytes(shit))