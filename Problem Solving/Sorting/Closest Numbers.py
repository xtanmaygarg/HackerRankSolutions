#!/bin/python3

import os

def closestNumbers(arr):
    arr.sort()
    L = len(arr)
    Answer = []
    Lowest = 10e15
    for i in range(1, L):
        Num = abs(arr[i] - arr[i - 1])
        if Num < Lowest:
            Lowest = Num
            Answer = []
            Answer.append(arr[i - 1])
            Answer.append(arr[i])
        elif Num == Lowest:
            Answer.append(arr[i - 1])
            Answer.append(arr[i])
        else:
            pass
    return Answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = closestNumbers(arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
