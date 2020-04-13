#!/bin/python

import os

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    A = [0] * 26
    B = [0] * 26
    for i in s1:
        A[ord(i) - 97] += 1
    
    for i in s2:
        B[ord(i) - 97] += 1
    
    Answer = 0
    for i in range(26):
        Answer += max(A[i], B[i]) - min(A[i], B[i])
    return Answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = raw_input()

    s2 = raw_input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
