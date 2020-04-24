#!/bin/python3

import os

def powerSum(X, N, Num):
    if X - Num ** N == 0:
        return 1
    elif X - Num ** N < 0:
        return 0
    else:
        return powerSum(X - Num ** N, N, Num + 1) + powerSum(X, N, Num + 1)
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    X = int(input())
    N = int(input())
    result = powerSum(X, N, 1)
    fptr.write(str(result) + '\n')
    fptr.close()
