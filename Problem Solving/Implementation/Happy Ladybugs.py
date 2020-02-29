#!/bin/python3

import os
from collections import Counter

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    C = Counter(b)
    if n == 1 and C['_'] == 0:
        return "NO"
    elif C['_'] == 1 and list(C.values()).count(1) == 1:
        return "YES"
    elif C['_'] > 1 and 1 not in C.values():
        return "YES"
    elif C['_'] == 0:
        for i in range(n):
            if i == 0:
                if b[i + 1] != b[i]:
                    return "NO"
            elif i == n - 1:
                if b[i - 1] != b[i]:
                    return "NO"
            else:
                if b[i + 1] != b[i] and b[i - 1] != b[i]:
                    return "NO"
        return "YES"
    else:
        return "NO"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
