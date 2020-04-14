#!/bin/python

import os

# Complete the lonelyinteger function below.
def lonelyinteger(a):
    A = 0
    for i in a:
        A = A ^ i
    return A

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    a = map(int, raw_input().rstrip().split())

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
