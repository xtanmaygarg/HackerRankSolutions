#!/bin/python3
# Please Run This Program in Pypy3

import os

def commonChild(s1, s2):
    N = len(s1)
    M = len(s2)
    DP = []
    for i in range(N + 1):
        DP.append([0] * (M + 1))

    for n in range(1, N + 1):
        for m in range(1, M + 1):
            if s1[n - 1] == s2[m - 1]:
                DP[n][m] = 1 + DP[n - 1][m - 1]
            else:
                DP[n][m] = max(DP[n - 1][m], DP[n][m - 1])
    return DP[N][M]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s1 = input()
    s2 = input()
    result = commonChild(s1, s2)
    fptr.write(str(result) + '\n')
    fptr.close()
