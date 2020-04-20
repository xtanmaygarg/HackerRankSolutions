#!/bin/python3

import os

def equalStacks(h1, h2, h3):
    h1.reverse()
    h2.reverse()
    h3.reverse()
    S1 = sum(h1)
    S2 = sum(h2)
    S3 = sum(h3)
    while(True):
        if min(S1, S2, S3) == 0:
            return 0
        if S1 == S2 and S1 == S3:
            return S1
        if max(S1, S2, S3) == S1:
            S1 -= h1.pop()
        elif max(S1, S2, S3) == S2:
            S2 -= h2.pop()
        elif max(S1, S2, S3) == S3:
            S3 -= h3.pop()


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
