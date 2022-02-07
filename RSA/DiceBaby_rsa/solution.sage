# https://eprint.iacr.org/2020/1059.pdf
# https://blog.soreatu.com/posts/intended-solution-to-crypto-problems-in-nctf-2019/#analysis-4

from Crypto.Util.number import long_to_bytes, bytes_to_long

p = 172036442175296373253148927105725488217
q = 337117592532677714973555912658569668821
N = 57996511214023134147551927572747727074259762800050285360155793732008227782157
e = 17
c = 19441066986971115501070184268860318480501957407683654861466353590162062492971
Z = ZZ.quotient_ring(N)
phi = (p-1)*(q-1)
d = inverse_mod(e, phi//e^4)

a = pow(c, d, N)

_phi = phi // e^4    
g_2 = pow(2, _phi, N)
g_3 = pow(3, _phi, N)
assert g_2 ^ e^2 == 1
assert g_3 ^ e^2 == 1


for i in range(0, e^2):
    for j in range(0, e^2):
        x, y = g_2^i, g_3^j
        m = long_to_bytes(int(a*x*y))
        if b"dice" in m:
            print(m)
