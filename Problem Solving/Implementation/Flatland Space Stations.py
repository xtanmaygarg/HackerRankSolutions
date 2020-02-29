#!/bin/python3

import os

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, m, c):
    if n == m:
        return 0
    else:
        c.sort()
        Ans = max(c[0] - 0, n - c[m - 1] - 1)
        for i in range(m - 1):
            L, R = c[i], c[i + 1]
            Avg = (L + R) // 2
            Ans = max(Ans, min(Avg - L, R - Avg))
        return Ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, m, c)

    fptr.write(str(result) + '\n')

    fptr.close()
