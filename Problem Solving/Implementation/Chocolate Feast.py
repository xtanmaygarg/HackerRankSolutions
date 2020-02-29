#!/bin/python3

import math
import os
import random
import re
import sys

# 6 2 2 === 3 + 
# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    first = n//c
    count = first
    while True:
        if first//m > 0:
            val = first//m
            count = count + val 
            rem = first - val * m
            first = rem + val
        else:
            break
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
