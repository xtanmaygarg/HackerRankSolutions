#!/bin/python

import os

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    Count = 0
    L = len(s)
    for i in range(L - 1):
        if s[i] == s[i + 1]:
            Count += 1
    return Count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
