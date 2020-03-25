#!/bin/python3

import os

# Complete the quickSort function below.
def quickSort(arr, n):
    Pivot = arr[0]
    left = []
    right = []
    for i in range(1, n):
        if arr[i] < Pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return (left + [Pivot] + right)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr, n)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
