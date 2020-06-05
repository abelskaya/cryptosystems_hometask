"""
Keys.py

Created by abelskaya.
Project cryptosystems_hometask

Генерация ключей
"""

import MillerRabin
import Math_Functions


def getPrimePair(bits=512):
    assert bits % 4 == 0

    p = MillerRabin.gen_prime(bits)
    q = MillerRabin.gen_prime_range(p + 1, 2 * p)

    return p, q


def generateKeys(nbits=1024):
    '''
    Генерация пары ключей:
        public = (e,n)
        private = d
    при этом n имеет длину nbits
    '''
    # nbits >= 1024 is recommended
    assert nbits % 4 == 0

    p, q = MillerRabin.getPrimePair(nbits // 2)
    n = p * q
    phi = Math_Functions.totient(p, q)

    # generate a d such that:
    #     (d,n) = 1
    good_d = False
    while not good_d:
        d = random.getrandbits(nbits // 4)
        if (Math_Functions.gcd(d, phi) == 1):
            good_d = True

    e = modInverse(d, phi)
    return e, n, d