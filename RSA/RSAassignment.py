import random

l1 = []
i = 2
while len(l1) != 300:
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        l1.append(i)
    i += 1

def miillerTest(d, n):
    a = 2 + random.randint(1, n - 4)
    x = pow(a, d, n)
 
    if (x == 1 or x == n - 1):
        return True
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;
 
        if (x == 1):
            return False;
        if (x == n - 1):
            return True;

    return False;

def isPrime( n, k):
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;

    d = n - 1;
    while (d % 2 == 0):
        d //= 2;

    for i in range(k):
        if (miillerTest(d, n) == False):
            return False;
 
    return True;

def generatePrime(n, k):
    num = int('1{}1'.format(''.join([str(random.randint(0, 1)) for _ in range(n - 2)])), 2)
    for i in l1:
        if i < num and num % i == 0:
            return generatePrime(n, k)
    else:
        if isPrime(num, k):
            return num
        else:
            return generatePrime(n, k)

def generateRSA():
    p = generatePrime(1024, 10)
    q = generatePrime(1024, 10)
    N = p * q
    phi = (p - 1) * (q - 1)
    e = 2 ** 16 + 1
    d = pow(e, -1, phi)
    return (N, e), (N, d)

publicKey, privateKey = generateRSA()

def enc(message):
    N, e = publicKey
    pt = ''
    for i in message:
        pt += hex(ord(i))[2:]
    pt = int(pt, 16)
    ct = pow(pt, e, N)
    return ct

def dec(ct):
    N, d = privateKey
    pt = pow(ct, d, N)
    pt = hex(pt)[2:]
    message = ''
    for i in range(0, len(pt), 2):
        message += chr(int(pt[i:i + 2], 16))
    return message

message = input("Input : ")
ct = enc(message)
pt = dec(ct)
print(pt)
assert(pt == message)