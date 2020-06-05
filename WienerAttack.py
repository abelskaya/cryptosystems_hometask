"""
WienerAttack.py 

Created by abelskaya.
Project cryptosystems_hometask
----
Атака Винера
"""

import Math_Functions

def Wiener(e, n):

    frac = Math_Functions.rational_to_contfrac(e, n)
    convergents = Math_Functions.convergents_from_contfrac(frac)

    for (k, d) in convergents:

        # check if d is actually the key
        if k != 0 and (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0 has integer roots
            discr = s * s - 4 * n
            if (discr >= 0):
                t = Math_Functions.is_perfect_square(discr)
                if t != -1 and (s + t) % 2 == 0:
                    print("Successfully hacked with Wiener attack!")
                    return d


def test_Wiener():
    print("Testing Wiener Attack")
    times = 5

    while (times > 0):
        e, n, d = Keys.generateKeys(1024)
        print("(e,n) is (", e, ", ", n, ")")
        print("d = ", d)

        hacked_d = Wiener(e, n)

        #         if d == hacked_d:
        #             print("Hack WORKED!")
        #         else:
        #             print("Hack FAILED")
        if d != hacked_d:
            print("Hack with Wiener attack FAILED")

        print("d = ", d, ", hacked_d = ", hacked_d)
        print("-------------------------")
        times -= 1


def apply_Wiener(e, N):
    print("Applying Wiener Attack")
    times = 1

    while (times > 0):
        print("(e,N) is (", e, ", ", N, ")")

        hacked_d = Wiener(e, N)

        print("hacked_d = ", hacked_d)
        print("-------------------------")
        times -= 1

# if __name__ == "__main__":
#
#     apply_Wiener(sys.argv[1], sys.argv[2])
