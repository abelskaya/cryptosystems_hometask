"""
RSA_Keys.py 

Created by abelskaya.
Project cryptosystems_hometask
----
Генерация ключей системы RSA
"""

import math
import random, sys
import Math_Functions, MillerRabin


def getPrimePair(bits=512):
    assert bits % 4 == 0

    p = MillerRabin.gen_prime(bits)
    q = MillerRabin.gen_prime_range(p + 1, 2 * p)

    return p, q


def generateKeysRSA(nbits=1024):
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
        if (gcd(d, phi) == 1):
            good_d = True

    e = modInverse(d, phi)
    return e, n, d


def testkeys():
    for i in range(2):
        e, n, d = generateKeysRSA()
        print("Public key:")
        print("e =")
        print(e)
        print("n =")
        print(n)
        print("Private key:")
        print("d =")
        print(d)
        print("-----------------------")