#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    D1 = dict()
    D2 = dict()
    D3 = dict()
    for i in range(n):
        D1[p[i]] = i + 1

    for i in range(n):
        D3[i + 1] = D1[D1[i + 1]]
    Ans = D3.values()

    return Ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
