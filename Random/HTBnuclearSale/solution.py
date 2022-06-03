# His information is encrypted below:
# pt ^ k
data1 = bytes.fromhex('6b65813f4fe991efe2042f79988a3b2f2559d358e55f2fa373e53b1965b5bb2b175cf039')

# Here is the ciphertext encrypted with our key.
# pt ^ k ^ k1
data2 = bytes.fromhex('fd034c32294bfa6ab44a28892e75c4f24d8e71b41cfb9a81a634b90e6238443a813a3d34')

# Encrypting again with our key...
# pt ^ k1
data3 = bytes.fromhex('de328f76159108f7653a5883decb8dec06b0fd9bc8d0dd7dade1f04836b8a07da20bfe70')

# data1 ^ data2 ^ data3 = pt ^ k ^ pt ^ k ^ k1 ^ pt ^ k1 
# = pt ^ pt ^ pt ^ k ^ k ^ k1 ^ k1                       [XOR is commutative]
# = pt ^ 0 ^ 0 ^ 0                                       [a ^ a = 0(Property of xor)]
# = pt                                                   [a ^ 0 = a(Property of xor)]

pt = []
for i in range(len(data1)):
    pt.append(data1[i] ^ data2[i] ^ data3[i])
print(bytes(pt))