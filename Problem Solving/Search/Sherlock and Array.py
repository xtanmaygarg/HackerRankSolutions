#!/bin/python3

import os

def balancedSums(arr):
    Sum = sum(arr)
    L = len(arr)
    Count = 0
    for i in range(L):
        if Sum - arr[i] - Count == Count:
            return "YES"
        Count += arr[i]
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
