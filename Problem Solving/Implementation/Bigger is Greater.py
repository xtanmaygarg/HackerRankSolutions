#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    List = list(w)
    i = len(List) - 1
    while i > 0 and List[i - 1] >= List[i]:
        i -= 1
    if i <= 0:
        return "no answer"
    
    j = len(List) - 1
    while List[j] <= List[i - 1]:
        j -= 1
    List[i - 1], List[j] = List[j], List[i - 1]
    
    List[i : ] = List[len(List) - 1 : i - 1 : -1]
    return ''.join(List)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    T = int(input())
    for T_itr in range(T):
        w = input()
        result = biggerIsGreater(w)
        fptr.write(result + '\n')
    fptr.close()
