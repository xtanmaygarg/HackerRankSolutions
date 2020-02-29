#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    cnt = [0]*k
    for x in s:
        cnt[x % k] += 1
    i, j, r = 1, k-1, 0
    if cnt[0] > 0:
        r += 1
    while i < j:
        r += max(cnt[i],cnt[j])
        i, j = i+1, j-1
    if i == j and cnt[i] > 0:
        r += 1
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
