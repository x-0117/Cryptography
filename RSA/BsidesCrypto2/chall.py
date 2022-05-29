from Crypto.Util.number import getPrime

flag = int.from_bytes(open("flag.txt","rb").read(), "big")

# Generate some RSA parameters
primes = [getPrime(1024) for _ in range(5)]
primes.sort()
moduli = [primes[i]*primes[i+1] for i in range(len(primes)-1)]
e = 65537

# Encrypt the flag 
for i,n in enumerate(moduli):
    flag = pow(flag, e, n)
    print(f"n{i+1}={n}")

print(f"{flag=}")