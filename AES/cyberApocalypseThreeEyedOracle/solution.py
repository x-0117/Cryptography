# -*- coding: utf-8 -*-
# The server accepts a user input and returns the following encrypted payload :
#     12 random bytes + userInput + flag

# The server is using the EBC mode of AES i.e each of the blocks get encrypted separately independent of one another.

# Exploit :
# Let's say the flag is "flag{abcd}"
# Let Random bytes : "XYZXYZXYZXYZ"
# We'll send a payload "A" * 34
#     Plaintext1 : XYZXYZXYZXYZAAAA | AAAAAAAAAAAAAAAA | AAAAAAAAAAAAAAAf | lag{abcd}PPPPPPP

# Also sending a brute forced payload : "A" * 34 + "a"
#                                       "A" * 34 + "b"
#                                       "A" * 34 + "c"
#                                       "A" * 34 + "d" and so on...
#     Plaintext2 : XYZXYZXYZXYZAAAA | AAAAAAAAAAAAAAAA | AAAAAAAAAAAAAAAa | flag{abcd}PPPPPP
#                  XYZXYZXYZXYZAAAA | AAAAAAAAAAAAAAAA | AAAAAAAAAAAAAAAb | flag{abcd}PPPPPP
#                  XYZXYZXYZXYZAAAA | AAAAAAAAAAAAAAAA | AAAAAAAAAAAAAAAc | flag{abcd}PPPPPP
#                  XYZXYZXYZXYZAAAA | AAAAAAAAAAAAAAAA | AAAAAAAAAAAAAAAd | flag{abcd}PPPPPP

# When we send the payload "A" * 34 + "f",
#     Plaintext2 becomes XYZXYZXYZXYZAAAA | AAAAAAAAAAAAAAAA | AAAAAAAAAAAAAAAf | flag{abcd}PPPPPP

# It can be observed that the 3rd block of pt1 and pt2 are the same and hence their encryptions will be the same.
# Therefore, we have found the 1st letter of the flag : 'f'

# Appending it to the flag variable : flag = 'f'

# Next set of payloads : 
#     "A" * 34 - len(flag)
#     Plaintext1 : XYZXYZXYZXYZAAAA | AAAAAAAAAAAAAAAA | AAAAAAAAAAAAAAfl | ag{abcd}PPPPPPPP

# Bruteforce payloads : "A" * 34 - len(flag) + flag + "a"
#                       "A" * 34 - len(flag) + flag + "b"
#                       "A" * 34 - len(flag) + flag + "c"
#                       "A" * 34 - len(flag) + flag + "d"
#     Plaintext2 : XYZXYZXYZXYZAAAA | AAAAAAAAAAAAAAAA | AAAAAAAAAAAAAAfa | flag{abcd}PPPPPP
#                  XYZXYZXYZXYZAAAA | AAAAAAAAAAAAAAAA | AAAAAAAAAAAAAAfb | flag{abcd}PPPPPP
#                  XYZXYZXYZXYZAAAA | AAAAAAAAAAAAAAAA | AAAAAAAAAAAAAAfc | flag{abcd}PPPPPP
#                  XYZXYZXYZXYZAAAA | AAAAAAAAAAAAAAAA | AAAAAAAAAAAAAAfd | flag{abcd}PPPPPP

# 3rd block matches when value of it's last character is 'l'. Hence we've found the 2nd character.
# Proceed in a similar manner...
                 
                      
from pwn import *
context.log_level = 'critical'

r = remote('157.245.33.77', 31268)

def main(shit):
    r.recvuntil(b'> ')
    r.sendline(shit.encode())
    received = r.recv()[:-1]
    return received[64:96]


flag = ''
ans = ''
while True:
    payload = '00' * (35 - len(ans))    # 19 + 16
    hex_ = main(payload)
    for i in range(32, 127):
        shit = main(payload + flag + hex(i)[2:])
        if shit == hex_:
            ans += chr(i)
            flag += hex(i)[2:]
            print(ans)
            break