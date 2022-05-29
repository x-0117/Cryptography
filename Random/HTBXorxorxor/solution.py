# ct[i] += pt[i] ^ key[i % len(key)]
# Flag format : HTB{...}
# ct[0], ct[1], ct[2], ct[3] known
# pt[0], pt[1], pt[2], pt[3] known
# key[i] = ct[i] ^ pt[i]
# Key is of 4 digit and we get the key

ct = bytes.fromhex('134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9')
knownPT = b'HTB{'
key = []
for i in range(4):
    key.append(knownPT[i] ^ ct[i])
pt = []
for i in range(len(ct)):
    pt.append(ct[i] ^ key[i % 4])
print(bytes(pt))

# HTB{rep34t3d_x0r_n0t_s0_s3cur3}