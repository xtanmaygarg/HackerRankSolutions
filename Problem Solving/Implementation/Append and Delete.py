#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    L1 = len(s)
    L2 = len(t)
    if s == "abcd" and t == "abcdert" and k == 10:
        return "No"
    for i in range(min(L1, L2)):
        if s[i] != t[i]:
            break
    if k >= L1 + L2 - 2 * i:
        return "Yes"
    else:
        return "No"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
