#!/bin/python

import os

def theGreatXor(x):
    Answer = 0
    Bit = 0
    while(x):
        if not x & 1:
            Answer += 1 << Bit
        x = x >> 1
        Bit += 1
    return Answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        x = int(raw_input())

        result = theGreatXor(x)

        fptr.write(str(result) + '\n')

    fptr.close()
