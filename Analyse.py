"""
Analyse.py

Created by abelskaya.
Project cryptosystems_hometask

"""

import os
import sys

import WienerAttack, pPollard

if __name__ == "__main__":

    e = sys.argv[1]
    e = int(e)
    N = sys.argv[2]
    N = int(N)

    WienerAttack.apply_Wiener(e,N)
    pPollard.apply_pPollard(e,N)
