#!/bin/python3

import os

def minimumSwaps(arr):
    Mapping = {}
    Swaps = 0
    for i in range(len(arr)):
        Mapping[arr[i]] = i
    
    for i in range(len(arr)):
        if arr[i] != i + 1:
            Num = arr[i]
            arr[i] , arr[Mapping[i + 1]] = arr[Mapping[i + 1]], arr[i]
            Mapping[Num] = Mapping[i + 1]
            Swaps += 1
            
    return Swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
