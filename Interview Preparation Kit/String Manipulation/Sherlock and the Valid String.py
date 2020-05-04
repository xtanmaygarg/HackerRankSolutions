#!/bin/python3

import os
from collections import Counter

def isValid(s):
    Count = Counter(s)
    Occurence = {}

    for i in Count:
        if Count[i] in Occurence:
            Occurence[Count[i]] += 1
        else:
            Occurence[Count[i]] = 1
    
    if len(Occurence) == 1:
        return "YES"
    elif len(Occurence) == 2:
        Keys = sorted(list(Occurence.keys()))
        if Keys[0] == 1 and Occurence[Keys[0]] == 1:
            return "YES"
        if (Keys[1] - Keys[0]) == 1 and Occurence[Keys[1]] == 1:
            return "YES"
        return "NO"
    return "NO"

    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = isValid(s)
    fptr.write(result + '\n')
    fptr.close()
