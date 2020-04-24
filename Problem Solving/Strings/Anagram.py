#!/bin/python3

import os

def anagram(s):
    A = [0] * 26
    B = [0] * 26
    L = len(s)
    if L & 1:
        return -1
    else:
        Ans = 0
        for i in range(L // 2):
            A[ord(s[i]) - 97] += 1
        for i in range(L // 2, L):
            B[ord(s[i]) - 97] += 1
        for i in range(26):
            Ans += abs(A[i] - B[i])
        return Ans // 2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
