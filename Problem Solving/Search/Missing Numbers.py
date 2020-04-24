#!/bin/python3

import os

def missingNumbers(arr, brr):
    Answer = []
    Count = {}
    for i in brr:
        if i in Count:
            Count[i] += 1
        else:
            Count[i] = 1
    
    for i in arr:
        Count[i] -= 1
    
    for i in Count:
        if Count[i]:
            Answer.append(i)
    Answer.sort()
    return Answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    m = int(input())
    brr = list(map(int, input().rstrip().split()))
    result = missingNumbers(arr, brr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
