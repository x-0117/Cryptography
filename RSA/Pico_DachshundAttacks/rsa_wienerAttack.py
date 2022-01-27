# -*- coding: utf-8 -*-

# Stolen shamelessly from https://github.com/pablocelayes/rsa-wiener-attack and arranged in a much less systematic manner...
# https://www.youtube.com/watch?v=OpPrrndyYNU

from Crypto.Util.number import long_to_bytes

def rational_to_contfrac(x,y):
    '''
    Converts a rational x/y fraction into
    a list of partial quotients [a0, ..., an]
    '''
    a = x//y
    pquotients = [a]
    while a * y != x:
        x,y = y,x-a*y
        a = x//y
        pquotients.append(a)
    return pquotients


def convergents_from_contfrac(frac):
    '''
    computes the list of convergents
    using the list of partial quotients
    '''
    convs = [];
    for i in range(len(frac)):
        convs.append(contfrac_to_rational(frac[0:i]))
    return convs


def contfrac_to_rational (frac):
    '''Converts a finite continued fraction [a0, ..., an]
     to an x/y rational.
     '''
    if len(frac) == 0:
        return (0,1)
    num = frac[-1]
    denom = 1
    for _ in range(-2,-len(frac)-1,-1):
        num, denom = frac[_]*num+denom, num
    return (num,denom)


def isqrt(n):
    '''
    Calculates the integer square root
    for arbitrary large nonnegative integers
    '''
    if n < 0:
        raise ValueError('square root not defined for negative numbers')
    
    if n == 0:
        return 0
    a, b = divmod(len(bin(n)) - 2, 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y


def is_perfect_square(n):
    '''
    If n is a perfect square it returns sqrt(n),
    
    otherwise returns -1
    '''
    h = n & 0xF; #last hexadecimal "digit"
    
    if h > 9:
        return -1 # return immediately in 6 cases out of 16.

    # Take advantage of Boolean short-circuit evaluation
    if ( h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8 ):
        # take square root if you must
        t = isqrt(n)
        if t*t == n:
            return t
        else:
            return -1
    
    return -1


def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = rational_to_contfrac(e, n)
    convergents = convergents_from_contfrac(frac)
    
    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr>=0):
                t = is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d


e = 1657805339429688812053143505041070479446292128411607570494243421760101704137301539086568061711572914192286708818311951491809958763731922974159879528048217191911809949318252855964312082817709188019888296969176903157632800355049328541044248401990090737592983323338514234850949188504162168586132574428719609765
N = 69946612833823474474567341713689184972332063124960313284323963391904325835001536564089987739039075606813821953828737052699889176170852295666471788226146362077823483434246648477714474043193142173165562623552641464965982360870678134642112700029973671619733747905675567176551945786098617460155171179688323257151
c_m = 29311486423187500425330376488764998659536706623004545634194705326716672050374070671117765893362655752130354154669903618594619025949342070080877875120252533550235579687317810364639488447285875968129203680724128585150906708070170492927818867527457559253200831533156258084726643270961969276171618824314271908005

d = hack_RSA(e, N)
plaintext = pow(c_m, d, N)

print(long_to_bytes(plaintext))

# picoCTF{proving_wiener_3878674}
