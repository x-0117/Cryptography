# Small value of e (e = 3)
# If pt < N ** 1/e, pt ** e < N.
# Therefore, ct = pow(pt, e, N) = pt ** e
# In this case pt = ct ** 1/3, if pt is small enough.

from factordb.factordb import FactorDB
from Crypto.Util.number import long_to_bytes

f = FactorDB(780865154948750571515875825956842965597268480061942498223759415931178548538528991182487495101556011494286950683286512165475038389107892269787484651054279065941410737793736223804092347531386151065849807188034668245557897119294115024094420977925386642701753372658008076601701)
f.connect()
factors = f.get_factor_list()

pt = 1
for i in set(factors):
    pt *= i

print(long_to_bytes(pt))
# HTB{n3v3r_us3_sm4ll_3xp0n3n7s_f0r_rs4}