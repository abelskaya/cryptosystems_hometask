"""
pPollard.py 
TODO
Created by abelskaya.
Project cryptosystems_hometask
----
Атака факторизации модуля p-методом Полларда
"""

import random
import math
from math import gcd
import Keys

def p_Pollard(n: int, x: int, y: int, stage: int, i: int):
    if bin(gcd(n, abs(x - y))) == 1:
        if i == stage:
            return p_Pollard(n, (x * x + 1) % n, x, stage * 2, i + 1)
        return p_Pollard(n, (x * x + 1) % n, y, stage, i + 1)
    else:
        print(gcd(n, abs(x - y)))
        return gcd(n, abs(x - y))


def test_pPollard():
    print("Testing p-Pollard Attack")
    times = 5

    while (times > 0):
        e, n, d = Keys.generateKeys(256)
        print("(e,n) is (", e, ", ", n, ")")
        print("d = ", d)

        x = random.randint(1, n - 2)
        y = 1
        i = 0
        stage = 2
        hacked_d = p_Pollard(n, x, y, stage, i)

        if d != hacked_d:
            print("Successfully hacked with p-Pollard attack!")
        else:
            print("Hack with p-Pollard attack FAILED")

        print("d = ", d, ", hacked_d = ", hacked_d)
        print("-------------------------")
        times -= 1


def apply_pPollard(e, N):
    print("Applying p-Pollard Attack")

    print("(e,n) is (", e, ", ", N, ")")

    x = random.randint(1, N - 2)
    y = 1
    i = 0
    stage = 2
    hacked_d = p_Pollard(N, x, y, stage, i)

    print("Successfully hacked with p-Pollard attack!")
    print("hacked_d = ", hacked_d)
    print("-------------------------")

