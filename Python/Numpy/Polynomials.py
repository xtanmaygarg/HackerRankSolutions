import numpy
Arr = list(map(float, input().split()))
N = int(input())
print(numpy.polyval(Arr, N))
