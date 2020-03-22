#!/bin/python3

import os

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    s = s.lower()
    L = len(s)
    H = 'hackerrank'
    i = 0
    j = 0
    while(i < 10 and j < L):
        if s[j] == H[i]:
            i += 1
        j += 1
    if i == 10:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
