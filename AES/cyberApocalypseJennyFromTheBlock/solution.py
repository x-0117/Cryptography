# -*- coding: utf-8 -*-
# Not an AES problem, but included in the category, owing to similarity.
# From the encryption code, it can be observed it's similar to a block cipher in CBC mode
# The message that is encrypted is 'command executed: ' + command + output
# The 1st block is encrypted with a random password. The password for encryption of the next block, depends on the previous pt block and ct block

# pt1    pt2    pt3    pt4    pt5    pt6    ...ptn
# ct1    ct2    ct3    ct4    ct5    ct6    ...ctn
#  pw     h2     h3     h4     h5     h6    ... hn

# Each of the pt, ct, h blocks are 16 bytes long
# Relation between pt, ct and ht : ct[i] = (pt[i] + h[i]) % 256                               (1)
# Relation between h(n), pt(n - 1) and ct(n - 1) : h(n) = sha256(pt(n - 1) + ct(n - 1))       (2)

# If we choose the command "cat secret.txt", we'll get the flag in the output'
# It's worth observing that if we choose the command "cat secret.txt", pt1 comes out to be b'Command executed' (1st 16 blocks of the message)
# Scince the server returns the encrypted message, ct1, ct2, ct3... ctn is known to us.
# From (2), h2  = sha256(ct1 + pt1)
# From (1), pt2 = (ct2 - h2) % 256

# In general, h(n)  = sha256(ct(n - 1) + pt(n - 1)) and
#             pt(n) = (ct(n) - h(n)) % 256

# Hence, we find pt1, pt2, pt3, ... ptn. And retreive the flag


from hashlib import sha256
shit = input(">>")
BLOCK_SIZE = 32
l1 = []

for i in range(0, len(shit), 2):
    l1.append(int(shit[i:i + 2], 16))
msg = b'Command executed: ' + b'cat secret.txt'
iv = []
for i in range(32):
    iv.append((l1[i] - msg[i]) % 256)

print(iv)

def encrypt_block(block, secret):
    enc_block = b''
    for i in range(BLOCK_SIZE):
        print(block[i], secret[i])
        val = (block[i]+secret[i]) % 256
        enc_block += bytes([val])
    return enc_block

en_block = l1[:32]
h = sha256(bytes(en_block) + msg).digest()

for i in range(32, len(l1), 32):
    msg1 = []
    for j in range(i, i + 32):
        msg1.append((l1[j] - h[j - i]) % 256)
    print(bytes(msg1))
    h = sha256(bytes(l1[i:i + 32]) + bytes(msg1)).digest()

# HTB{b451c_b10ck_c1ph3r_15_w34k!!!}
