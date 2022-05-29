# -*- coding: utf-8 -*-
# AES encryption using ECB mode
# Accepts an integer M from user
# Computes shared_secret = M ** c (mod p)
# Computes key = md5(shared_secret)
# Accepts message from user.
# Decrypts the message uding the key
# Compares the message with b"Initialization Sequence - Code 0"
# returns flag if the the two are the same

# pt is known.
# If somehow the key can be controlled, we can send an encrypted message using the same key over the server, which when decrypted(with the samew key) and compared would return a positive result
# For the key to be known, shared_secret has to be a known value
# shared_secret = M ** c (mod p), c unknown
# For M = 1, shared_secret == 1 for all c.
# There fore we're sending the message encrypted with shared_secret = 1, and getting the flag


from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes, bytes_to_long
import hashlib

def encrypt(message, shared_secret):
    key = hashlib.md5(long_to_bytes(shared_secret)).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(message)

print(bytes_to_long(encrypt(b"Initialization Sequence - Code 0", 1)))

# HTB{7h15_p2070c0l_15_pr0tec73d_8y_D@nb3er_c0pyr1gh7_1aws}