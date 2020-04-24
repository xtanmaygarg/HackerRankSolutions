#!/bin/python3

import os

# Complete the marsExploration function below.
def marsExploration(s):
    Len = len(s)
    L = Len // 3
    Ans = 0
    Real = 'SOS' * L
    for i in range(Len):
        if s[i] != Real[i]:
            Ans += 1
    return Ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = marsExploration(s)
    fptr.write(str(result) + '\n')
    fptr.close()
