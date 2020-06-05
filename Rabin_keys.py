"""
Rabin_keys.py 

Created by abelskaya.
Project cryptosystems_hometask
----
Генерация ключей системы Рабина
"""

import math
import random, sys
import Math_Functions, MillerRabin, RSA_Keys


def generateKeysRabin(nbits=1024):
    # nbits >= 1024 is recommended
    assert nbits % 4 == 0

    p, q = MillerRabin.getPrimePair(nbits // 2)
    n = p * q

    return n, p, q


def cipherRabinKey(nbits=1024, m):
    e, n, d = RSA_Keys.generateKeysRSA(256)

    while m >= n:
        e, n, d = RSA_Keys.generateKeysRSA(256)

    c = pow(m, e, n)

    return c
