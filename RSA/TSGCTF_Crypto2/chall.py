# Minimalist's Private
from Crypto.Util.number import isPrime
from random import randrange
from secret import p, q, L, e, d

class RSA:
    def __init__(self, p, q, L, e, d):
        assert(isPrime(p) and isPrime(q))
        self.N = p * q
        self.L = L
        self.e = e
        self.d = d

        # these are the normal RSA conditions
        for _ in range(100):
            assert(pow(randrange(1, self.N), self.L, self.N) == 1)
        assert(self.e * self.d % self.L == 1)

        # minimal is the best
        assert(self.L * self.L <= 10000 * self.N)

    def gen_private_key(self):
        return (self.N, self.d)

    def gen_public_key(self):
        return (self.N, self.e)

    def encrypt(self, msg):
        return pow(msg, self.e, self.N)

    def decrypt(self, c):
        return pow(c, self.d, self.N)

flag = open('flag.txt', 'rb').read()
msg = int.from_bytes(flag, byteorder='big')
assert(msg < p * q)

rsa = RSA(p, q, L, e, d)
encrypted = rsa.encrypt(msg)
assert(rsa.decrypt(encrypted) == msg)

print(f'N, e = {rsa.gen_public_key()}')
print(f'c = {encrypted}')



# N, e = (1108103848370322618250236235096737547381026108763302516499816051432801216813681568375319595638932562835292256776016949573972732881586209527824393027428125964599378845347154409633878436868422905300799413838645686430352484534761305185938956589612889463246508935994301443576781452904666072122465831585156151, 65537)
# c = 254705401581808316199469430068831357413481187288921393400711004895837418302514065107811330660948313420965140464021505716810909691650540609799307500282957438243553742714371028405100267860418626513481187170770328765524251710154676478766892336610743824131087888798846367363259860051983889314134196889300426
