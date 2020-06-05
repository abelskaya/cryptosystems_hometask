"""
Miller-Rabin.py 
TODO
Created by abelskaya.
Project cryptosystems_hometask
----
Генерация простых чисел при помощи алгоритма Миллера-Рабина
"""

import random
import math


def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    i = 0
    # Invariant: a_to_power = a^(d*2^i) mod n

    # we test whether (a^d) = 1 mod n
    if a_to_power == 1:
        return True

    # we test whether a^(d*2^i) = n-1 mod for 0<=i<=s-1
    while (i < s - 1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
        i += 1

    # we reach here if the test failed until i=s-2
    return a_to_power == n - 1


def miller_rabin(n):
    # Compute s and d such that n-1 = (2^s)d, with d odd
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1

    # Applies the test K times
    # The probability of a false positive is less than (1/4)^K
    K = 20

    i = 1
    while (i <= K):
        # 1 < a < n-1
        a = random.randrange(2, n - 1)
        if not miller_rabin_pass(a, s, d, n):
            return False
        i += 1

    return True


def gen_prime(nbits):
    while True:
        p = random.getrandbits(nbits)
        # force p to have nbits and be odd
        p |= 2 ** nbits | 1
        if miller_rabin(p):
            return p
            break


def gen_prime_range(start, stop):
    while True:
        p = random.randrange(start, stop - 1)
        p |= 1
        if miller_rabin(p):
            return p
            break


def test_MR(name, n):
    if name == "test":
        print(miller_rabin(n) and "PRIME" or "COMPOSITE")
    elif name == "genprime":
        nbits = int(n)
        print(gen_prime(nbits))