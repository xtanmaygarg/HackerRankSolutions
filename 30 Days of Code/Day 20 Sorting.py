#!/bin/python3
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
L = len(a)
Count = 0
for i in range(L):
    for j in range(i + 1, L):
        if a[i] > a[j]:
            Count += 1
            a[i], a[j] = a[j], a[i]
print("Array is sorted in " + str(Count) + " swaps.")
print("First Element:", a[0])
print("Last Element:", a[-1])
