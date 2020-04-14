#!/bin/python

import os

def theLoveLetterMystery(s):
    N = len(s)
    i = 0
    j = N - 1
    Answer = 0
    while(i < j):
        Answer += abs(ord(s[i]) - ord(s[j]))
        i += 1
        j -= 1
    return Answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(raw_input())
    for q_itr in xrange(q):
        s = raw_input()
        result = theLoveLetterMystery(s)
        fptr.write(str(result) + '\n')
    fptr.close()
