#!/bin/python3

import os

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    A = [0] * 26
    B = [0] * 26
    for i in a:
        A[ord(i) - 97] += 1
    
    for i in b:
        B[ord(i) - 97] += 1
    
    Answer = 0
    for i in range(26):
        Answer += max(A[i], B[i]) - min(A[i], B[i])
    return Answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
