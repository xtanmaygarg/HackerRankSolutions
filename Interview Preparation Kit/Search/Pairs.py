#!/bin/python3
import os

def pairs(k, arr):
    Mapping = dict()
    for i in arr:
        Mapping[i] = True
    Answer = 0
    for i in arr:
        if i + k in Mapping:
            Answer += 1
    return Answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
