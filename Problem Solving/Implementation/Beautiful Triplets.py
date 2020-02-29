#!/bin/python3

import math
import os

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    Dict = dict()
    for i in arr:
        Dict[i] = True
    Ans = 0
    X = 0

    for i in arr:
        try:
            X = Dict[i + d] + Dict[i + d + d]
            Ans += 1
        except Exception:
            pass
    return Ans
        




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
