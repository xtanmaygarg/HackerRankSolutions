#!/bin/python3

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    Num = arr[-1]
    i = n - 1
    while(arr[i - 1] > Num):
        arr[i] = arr[i - 1]
        print(*arr)
        i -= 1
        if i == 0:
            break
    arr[i] = Num
    print(*arr)
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)
