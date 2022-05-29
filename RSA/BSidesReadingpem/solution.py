# -*- coding: utf-8 -*-
# I sent the private key instead of the public one. If you know how to read a private key, I'm done!

# SOLUTION
from Crypto.Util.number import long_to_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

shit = """-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAsx5R2YQtDn74JBEmUSZGnM4U4bVIpy9jI2C0b+vJ7xeEi6sU
IgVOA3IJ9/0Vhy3h+CQwtX1YEO5VZER/q/AOjJ5JBcjKnykOUZK+AoWr3B7gV1Mp
JAfExIyWnPUN3unhfXakU3xjSEI0QkIdOZhjbKbZTqqmJFDjPzxnCw1SsGv5Xd5W
E0lZQD8dI96Kv9f/HazR6XSZ7w7PaK7BYDXchQDlKh80UBw3KIC86kw/FhBmp+vl
1Aa4TcWyMXLNM/4W9CbdDphi4MNo+Uk5JanYVg2Iw92xkZsAT6Uasis0w6WEf/Bj
xVGSzFwaKRAgMVdz1/xGKR+iPF5qvTKjQOAxiwIDAQABAoIBAQCmGy/8b774+nZT
vDO0fbJuKA7lYaCGqkNdw4iRYjBaMY0RmQ2KnzDBsTfdai5UthAgdi9Vn2/UA7Hc
0kkzweM8NG2zl4mQIBrPOy5KWHwQHfIeCVjVuP6Y52elFvxOBMa/+w5Y/bl0gTDF
YVqI1vEdCX3sngSFGR4kvncwoKJWR7376tapV0dybFpufYlVTHL3PxvN6qI65E3K
iCu59NhmQ32RphLDViUiHinUxrO8FZQPJf0dUyiUpSAnhWmLPfFX2x4gF9wC66C+
Lv2fdS7x4jv4jrJQ0FJuMw4XGCMJETa7ckehkcRp99Sj33PfSJR9J4xuZoS4QJx3
aSSBMiXBAoGBAM4RbJDRuIH/7y9SDYwXOzd5nEaIN2+iy7bN6dJEzXadOtulDNNl
+K7J5RIjSfXvkldrEQZRQxNT0FcIz+rAqKWYcr2pOTFtBGbOmM2wEJSjjjD7Akvx
bzZ7tUUBYHv7NIxnT4lF5j032/0PixW1B9ndppji61Ta4Ha2ZmlETUq/AoGBAN6F
MAQM+P8bs2Iy5ihUnSY/eARD7b1UoBCORq1Az0RDHHSFfpitlJ6b2zQ3lw7gKQGj
QMpEdNW0LjefOmJUb3Ae5P4W3Xlidfh0SR7wWM7N9Lhq1GjUOPvxOweNyaJvu0Xi
Vl55hC2IHZaHqNzMDeAcp8p/pWljfcxuj/4Ypkg1AoGBAKnwpqbbvZzAE2Hj+jYg
5n3+dYmZRpZzHCs6r2zvvr3mNqby+5vPCYIkEBygK5t9oiMjsduS4o0q3rMYGleP
4MUH7wBIcVk4fZvHHy7p1xKtu1Lbfm5gwoWdCcXJt+cnKJPtkyMzGQg9a9fLnLkf
HUVnzL9izA6jnt9n1xdS86cDAoGBALemgueE8WhTK2zrh0tX8k9j6KDUk31EP8sK
McjCCY5UOULt/nryIAv7pCHnk3PCi/V/EHUfpLHPwKlFcEFBYKvPw7z1kBqjqavC
BatUQGeGUeh2uxI9vT4qbUahvf2ja5OU5yWX8wBFK+5VzodUnksOO2mEijd91pCH
262iGHLVAoGACh+k4BSIL0HFINZOGKzaNGtK5dn7WbVE+an3ebdAXDXfEHm+bKiK
cBwuNKWmbUFO5iucN112SQjMjY2P8REjUMIXAMu0/TpGPQq1OUlRNAiyLKJ71nlY
P8qlpiifNNbP1kxylxRWHFwHXheXkUUlqB4qnWKTLMPs/1fEQjt6dqk=
-----END RSA PRIVATE KEY-----
"""

shit = RSA.importKey(shit)

n = shit.n
e = shit.e
d = shit.d
p = shit.p
q = shit.q

key = RSA.construct((n, e, d))
cipher = PKCS1_OAEP.new(key)

c = bytes.fromhex("25a4445f7a890e9d0e9ce5a31380d5a504c3083197cc0e191b37c9c670dbefbde74c21efce911e1d331e28fc1bd24ac0d9682028f2c9fad9de6bde5c0f2df6a64a2b94cdd1ba311db6e36d9b41b0e2d40a25cdf9fefc57971cec972f9c39cc79d8e8ce20d1968f58e4e2390928927cbc17d294653cd483a3b6b2b561d957a569c5729526f1240b2ece6d8213fbc18ebdd32a15b904f0ded8af11d3f3e59e71a6ab5a206805762e88e6eea8fe1f14aa277e542faaf2cfc2050a4a0e8b8b5f242e35869b6cab81f022a831c04c621f67abf25a74e419f1f4ef056225efeb95bccb15bff2bf7fe04f0dd359a181c7c37821420adeef4729d767b51067d60c6f4167")
print(cipher.decrypt(c))

# flag{c0ngr47s_u_c4n_r34d_93m}