#!/bin/python

import os

# Complete the superDigit function below.
def superDigit(n, k):
    if n < 10:
        return n
    else:
        S = sum(list(map(int, list(str(n)))))
        if k == 0:
            if S < 10:
                return S
            else:
                return superDigit(S, 0)
        S = S * k
        return superDigit(S, 0)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
