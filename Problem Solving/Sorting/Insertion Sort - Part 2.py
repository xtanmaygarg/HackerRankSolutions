#!/bin/python3

def insertionSort2(n, arr):
    for i in range(1, n):
        Num = arr[i]
        j = i - 1
        while(j > -1):
            if Num > arr[j]:
                break
            else:
                arr[j + 1] = arr[j]
                j -= 1
        
        arr[j + 1] = Num
        print(*arr)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)
