#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    t = s[::-1]
    s = list(s)
    t = list(t)
    sl = []
    tl = []
    fl = []
    gl = []
    for i in s:
        sl.append(ord(i))
    for i in t:
        tl.append(ord(i))
    for i in range(0,len(sl)-1):
        fl.append(abs(sl[i+1] - sl[i]))
    for i in range(0,len(tl)-1):
        gl.append(abs(tl[i+1] - tl[i]))
    #print(gl)
    print(fl)
    if fl == gl:
        return "Funny"
    else:
        return "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
