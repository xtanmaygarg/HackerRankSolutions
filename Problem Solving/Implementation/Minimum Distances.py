#!/bin/python3

import os

# Complete the minimumDistances function below.
def minimumDistances(a):
    val = []
    for i in a:
        t = a.index(i)
        for num in range(a.index(i)+1,len(a)):
            if a[num] == i:
                val.append(num-t)
    if len(val) == 0:
        return -1
    return min(val)


        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
