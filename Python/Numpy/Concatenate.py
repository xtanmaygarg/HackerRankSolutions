import numpy
N, M, P = map(int, input().split())
Arr = []
Arr2 = []
for i in range(N):
    Arr.append(list(map(int, input().split())))

for i in range(M):
    Arr2.append(list(map(int, input().split())))

print(numpy.concatenate((Arr, Arr2), axis = 0))
