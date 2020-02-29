#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    N = math.ceil((p - m) / d) + 1
    L = p - (N - 2) * d
    SN = ((N - 1) * (p + L)) // 2
    # print(L, SN)
    if SN < s:
        Ans = N - 1
        Rem = s - SN
        Ans += Rem // m
    else:
        Ans = -1
        while(s > 0):
            s -= p
            p -= d
            Ans += 1
    return Ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

fptr.write(str(answer) + '\n')

fptr.close()
