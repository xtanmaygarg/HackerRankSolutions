#!/bin/python3

import os
from collections import defaultdict

def countTriplets(arr, r):
    TwoLength = defaultdict(int)
    ThreeLength = defaultdict(int)
    Answer = 0

    for i in arr:
        Answer += ThreeLength[i]
        ThreeLength[i * r] += TwoLength[i]
        TwoLength[i * r] += 1
    return Answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
