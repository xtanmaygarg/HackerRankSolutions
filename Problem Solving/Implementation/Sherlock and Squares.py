#!/bin/python3

from math import sqrt
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    count = 0
    x = int(sqrt(a))
    y = int(sqrt(b))
    for i in range(x,y+1):
        if i*i >= a and i*i <= b:
            count = count + 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
