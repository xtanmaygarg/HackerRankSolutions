#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    if m % n == 0 and s != 1:
        return s - 1
    elif m % n == 0 and s == 1:
        return n
    elif s + (m % n) - 1 <= n:
        return s + (m % n) - 1
    else:
        return (s + (m % n) - 1) % n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
