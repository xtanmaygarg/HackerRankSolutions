#!/bin/python

import os

# Complete the sumXor function below.
def sumXor(n):
    if n == 0:
        return 1
    N = bin(n)
    return 2 ** (N.count('0') - 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
