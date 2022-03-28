# -*- coding: utf-8 -*-

# We connected to a remote server
# The server would encrypt and decrypt our messages for us
# The server will encrypt everything except the string 'd4r3d3v!l'
# The server will give us the flag if we provided the correct encryption for 'd4r3d3v!l'

from pwn import *
from Crypto.Util.number import long_to_bytes, bytes_to_long
context.log_level = 'critical'

r = remote('chall.nitdgplug.org', 30093)

r.recvuntil(b'>')
r.sendline(b'P')
r.recv()
shit = r.recv()
N = int(shit.decode().split(':')[1].strip()[2:], 16)
e = int(r.recv().decode().split(':')[1].strip()[2:-3], 16)

r.sendline(b'S')
print(r.recv())


k = 2
TOKEN = b'd4r3d3v!l'
pt1 = bytes_to_long(TOKEN)
pt = hex((pow(k, e, N) * pt1) % N)[2:]
r.sendline(pt.encode())
shit = r.recv()
print(shit)
ct = int(shit.decode().split(':')[1].strip()[2:], 16)
print(ct)
print(r.recv())


ct1 = (ct * pow(k, -1, N)) % N


r.sendline(b'V')
print(r.recv())

r.sendline(hex(pt1)[2:].encode())
# r.sendline(b'ff')
print(r.recv())

r.sendline(hex(ct1).encode())
# r.sendline(hex(signed).encode())
print(r.recv())
print(r.recv())


r.close()
