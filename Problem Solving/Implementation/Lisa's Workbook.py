#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    PageNum = 1
    Special = 0
    for i in arr:
        Prob = 1
        if i >= k:
            while(i >= k):
                if PageNum in range(Prob, Prob + k):
                    Special += 1
                PageNum += 1
                Prob += k
                i -= k
                if i < k and i != 0:
                    if PageNum in range(Prob, Prob + i):
                        Special += 1
                    PageNum += 1
        else:
            if PageNum in range(Prob, Prob + i):
                Special += 1
            PageNum += 1
        print(Special, PageNum)
    return Special

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
