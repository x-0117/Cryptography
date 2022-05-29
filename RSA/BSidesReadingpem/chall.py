from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import getPrime, inverse

p,q = getPrime(1024),getPrime(1024)
n = p * q
e = 65537
phi = (p-1)*(q-1)
d = int(inverse(e, phi))
key = RSA.construct((n, e, d, p, q))
rsa = PKCS1_OAEP.new(key)
print(key.exportKey().decode())
print(rsa.encrypt(open('./flag.txt', 'rb').read()).hex())