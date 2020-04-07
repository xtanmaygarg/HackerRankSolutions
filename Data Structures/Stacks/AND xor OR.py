#!/bin/python3

import os

def andXorOr(Arr, N):
    Max = -1
    Stack = []
    for i in range(N):
        while Stack:
            Max = max(Arr[i] ^ Stack[-1], Max)
            if Stack[-1] > Arr[i]:
                Stack.pop()
            else:
                break
        Stack.append(Arr[i])
    return Max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a_count = int(input())
    a = list(map(int, input().rstrip().split()))
    result = andXorOr(a, a_count)
    fptr.write(str(result) + '\n')
    fptr.close()
