"""
Math_Functions.py 
TODO
Created by abelskaya.
Project cryptosystems_hometask
----

"""

import math
import random, sys



def egcd(a, b):
    '''
    Расширенный алгоритм Евклида
    Возвращает x, y, gcd(a,b) такие, что ax + by = gcd(a,b)
    '''
    u, u1 = 1, 0
    v, v1 = 0, 1
    while b:
        q = a // b
        u, u1 = u1, u - q * u1
        v, v1 = v1, v - q * v1
        a, b = b, a - q * b
    return u, v, a


def gcd(a, b):
    '''
    Работает быстрее, чем стандартный gcd
    '''
    a, b = (b, a) if a < b else (a, b)

    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    '''
    Подсчёт НОК
    '''
    return (a * b) // math.gcd(a, b)


def modInverse(e, n):
    '''
    Возвращает d: de = 1 (mod n)
    e должно быть взаимно просто с n
    '''
    return egcd(e, n)[0] % n


def totient(p, q):
    return (p - 1) * (q - 1)


def bitlength(x):
    '''
    Вычисление битовой длины x
    '''
    assert x >= 0
    n = 0
    while x > 0:
        n = n + 1
        x = x >> 1
    return n


def sieve(n: int) -> list:
    """
    Sieve away and only primes are left.
    """
    primes = 2 * [False] + (n - 1) * [True]
    for i in range(2, int(n ** 0.5 + 1.5)):
        for j in range(i * i, n + 1, i):
            primes[j] = False
    return [prime for prime, checked in enumerate(primes) if checked]


def isqrt(n):
    if n < 0:
        raise ValueError('Квадратный корень не вычисляется для отрицательных чисел')

    if n == 0:
        return 0
    a, b = divmod(bitlength(n), 2)
    x = 2 ** (a + b)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


def is_perfect_square(n):
    '''
    Возвращает квадратный корень, если число -- полный квадрат,
    и -1 -- в противном случае
    '''
    h = n & 0xF;

    if h > 9:
        return -1

    if (h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8):

        t = isqrt(n)
        if t * t == n:
            return t
        else:
            return -1

    return -1

def rational_to_contfrac(x,y):
    '''
    Converts a rational x/y fraction into
    a list of partial quotients [a0, ..., an]
    '''
    # x = int(x)
    # y = int(y)
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