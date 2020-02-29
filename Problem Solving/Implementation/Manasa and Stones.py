#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stones function below.
def stones(n, a, b):
    Min = min(a, b)
    Max = max(a, b)
    Ans = set()
    for i in range(1, n + 1):
        Ans.add(Min * (n - i) + Max * (i - 1))
    Result = list(Ans)
    Result.sort()
    return Result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
