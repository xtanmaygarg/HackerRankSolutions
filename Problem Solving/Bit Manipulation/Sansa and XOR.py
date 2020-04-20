#!/bin/python3

import os

# Complete the sansaXor function below.
def sansaXor(arr):
    if n & 1:
        Ans = 0
        for i in range(0, n, 2):
            Ans = Ans ^ arr[i]
        return Ans
    else:
        return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
