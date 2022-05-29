# -*- coding: utf-8 -*-

# The flag is being encrypted by a random key (which is also the iv) in CBC mode using AES
# The shuffled key is also returned
# From the code it can be seen that the key has been shuffled using random.shuffle() function with a given seed
# The seed set before calling the shuffle() function is a random number which lies in between the two smallest bytes in the key
# That didn't work so, I bruteforced all values from 0 - 256

# Took a known array of length 16 : l2 = list(range(16))
# Shuffled the array with a given seed, s : random.seed(s); random.shuffle(l2)
# Rearranged the byte positions in a new array ans according to the byte positions in the shuffled array to get the deshuffled(original) key for the given seed.
# (For a given seed, and for a given size of an array, an element at a given index i will ALWAYS shift to a given location j) 
# Eg : For an array of length 16, for seed 10, the element at the 2nd index will always shift to the 0th index
# Decrypt with the obtained key
# Check whether the obtained string starts with b'flag' (Known plaintext)

# The original data was lost so relayed thew atack with flag : flag{example_flag12345678901234}
# encrypted_flag = 8b81942f6b24ac763b282663185750001081767876507b1363bc4596b3cbaee7
# obfuscated_key = 7443868a5eb7f8c490ad9a6325d0372a


import os
from Crypto.Cipher import AES
import random

for s in range(0, 256):
    l1 = bytes.fromhex("7443868a5eb7f8c490ad9a6325d0372a")
    
    random.seed(s)
    l2 = list(range(len(l1)))
    random.shuffle(l2)
    ans = [-1 for _ in range(len(l1))]
    for i in range(len(l1)):
        ans[i] = l1[l2.index(i)]
    key = bytes(ans)

    cipher = AES.new(key, AES.MODE_CBC, key)
    encrypted_flag = bytes.fromhex("8b81942f6b24ac763b282663185750001081767876507b1363bc4596b3cbaee7")

    flag = cipher.decrypt(encrypted_flag)
    
    if b'flag' in flag:
        print(flag)