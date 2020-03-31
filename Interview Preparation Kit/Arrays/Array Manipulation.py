#!/bin/python3

import os

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    Array = [0] * n
    for a, b, k in queries:
        Array[a - 1] += k
        if b < n:
            Array[b] -= k

    X = 0
    Max = 0
    for i in Array:
        X += i
        Max = max(X, Max)
    
    return Max
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().split())))

    result = arrayManipulation(n, queries)
    fptr.write(str(result) + '\n')

    fptr.close()
