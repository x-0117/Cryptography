# -*- coding: utf-8 -*-

# The question's based on key envelopping
# It's a concept that utilizes both the fast nature of symmetric key encryption and the safe key transfer of asymmetric key encryption
# The pt is encrypted with a key, k1 using AES
# The key k1 is encrypted with the receiver's public key

# Key k1 is decrypted using receiver's private key (n was factored using factordb.com)
# pt was decrypted using k1 as key

from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
shit = RSA.importKey(open('C:/Users/User/Desktop/pubkey.pem', 'r').read())


# Retreiving symmetric key
n = shit.n
e = shit.e

# From factordb.com
p = 1128137999850045612492145429133282716267233566834715456536184965477269592934207986950131365518741418540788596074115883774105736493742449131477464976858161587355643311888741515506653603321337485523828144179637379528510277430032789458804637543905426347328041281785616616421292879871785633181756858096548411753919440011378411476275900648915887370219369154688926914542233244450724820670256654513052812215949495598592852131398736567134556141744727764716053145639513031
phi = p * (p - 1) * (p - 1)
d = pow(e, -1, phi)
key = int(open('C:/Users/User/Desktop/key', 'r').read(), 16)
key_decrypted = long_to_bytes(pow(key, d, n))


# Retreiving the flag (Cipher text)
cipher = AES.new(key_decrypted, AES.MODE_ECB)
shit = open('C:/Users/User/Desktop/flag.txt.aes', 'rb').read()
print(cipher.decrypt(shit[:-1]))