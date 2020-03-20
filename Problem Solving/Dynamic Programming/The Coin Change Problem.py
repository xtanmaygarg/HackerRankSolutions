#!/bin/python3

import math
import os
import random
import re
import sys

def getWays(n, c):
    DP = []
    for i in range(len(c)):
        DP.append([0] * (n + 1))

    for i in range(len(c)):
        for j in range(n + 1):    
            if j < c[i]:
                if c[i] == 1:
                    continue
                else:
                    DP[i][j] = DP[i - 1][j]
            elif c[i] == 1:
                DP[i][j] = 1
            elif c[i] == j:
                DP[i][j] = DP[i - 1][j] + 1
            else:
                DP[i][j] = DP[i - 1][j] + DP[i][j - c[i]]
    return DP[len(c) - 1][n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    c = list(map(int, input().rstrip().split()))
    c.sort()
    ways = getWays(n, c)
    fptr.write(str(ways) + '\n')
    fptr.close()
