# Difficult isn't the right word to describe this question, annoying is!
# (Here, the word 'flag' is used to reference a randomly generated integer on the basis of which desicions are being taken)
# for pt[i], output[2 * i] = ct[i] and output[2 * i + 1] = flag[i] ^ 0x4a
# On the basis of the value of flag[i], certain operations are done on the plaintext[i].

# output[2 * i + 1] is xorred with 0x4a for all possible i
# In order to obtain pt from ct:
#     The conditions on flag[i] are checked.
#     If true, the operation applied is queued.
#     The inverse operation of each of the queued operations is applied on pt in an inversed manner
#     Eg: If ct[i] = op1(op2(pt[i])) then pt[i] = op2'(op1'(ct[i])), where op' is inverse function of op
# Find all pt[i] and concatenate to get flag(string to be submitted).

# Inverse operations for XorBy6B(char), XorBy3E(char), NegateChar(char) are the same as the functions themselves.
# For ESwapChar, there are some changes.


import math

shit = [int(_) for _ in '108 182 82 176 167 158 69 222 39 102 234 14 241 16 10 218 160 108 76 234 225 224 1 12 97 122 114 90 10 90 250 14 155 80 101 186 97 218 115 218 207 76 190 174 196 84 192 144'.split()]
chars = []
flags = []

for i in range(0, len(shit), 2):
    chars.append(shit[i])
    flags.append(shit[i + 1] ^ 0x4A)


strchr = lambda x: chr(x)
strbyt = lambda x, y=0: ord(x[y])
bitlst = lambda x, y: x << y
bitrst = lambda x, y: x >> y
bitext = lambda x, y, z=1: bitrst(x, y) & int(math.pow(2, z) - 1)
bitxor = lambda x, y: x ^ y
bitbor = lambda x, y: x | y
btest  = lambda x, y: (x & y) != 0

def ValidateChar(char):
    if type(char) is str and len(char) == 1:
        r = strbyt(char)
    return char

def CheckFlag(f, flag):
    return btest(f, flag)

def ESwapChar(char):
    char = bin(char)[2:].rjust(8, '0')
    MSB = char[:4]
    LSB = char[4:]
    MSB = bin(int(MSB, 2) ^ 0b1011)[2:].rjust(4, '0')
    LSB = bin(int(LSB, 2) ^ 0b1101)[2:].rjust(4, '0')
    char = int(LSB + MSB, 2)
    return char

def XorBy6B(char):
    return char ^ 0x6b

def XorBy3E(char):
    return char ^ 0x3e

def NegateChar(char):
    # char = ValidateChar(char)
    return 255 - char


# print(NegateChar(NegateChar(62)))
def decryptCharacter(char, flag):
    if CheckFlag(flag, 16):
        char = XorBy3E(char)
    if CheckFlag(flag, 8):
        char = XorBy6B(char)
    if CheckFlag(flag, 2):
        char = NegateChar(char)
    if CheckFlag(flag, 64):
        char = ESwapChar(char)
    return chr(char)

for i in range(len(flags)):
    print(decryptCharacter(chars[i], flags[i]), end = '')

# HTB{Lun4_Lu4_L4t1n_M00n}