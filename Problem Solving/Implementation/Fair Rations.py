#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    count = 0
    for i in B:
        if len(B) == 2 and (B[0]+B[1])%2==1:
            return "NO"
        if i%2 == 1:
            count = count + 2
            index = B.index(i)
            B[index] += 1
            if index != len(B):
                try:
                    B[index+1] += 1
                except IndexError:
                    return "NO"
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
