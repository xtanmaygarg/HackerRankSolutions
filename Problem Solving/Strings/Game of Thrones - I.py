#!/bin/python

import os

def gameOfThrones(s):
    Words = [0] * 26
    for i in s:
        Words[ord(i) - 97] += 1
    
    Odd = 0
    for i in Words:
        if i & 1:
            Odd += 1
    if Odd < 2:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
