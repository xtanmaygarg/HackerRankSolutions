import numpy

N, M = map(int, input().split())
Arr = []
for i in range(N):
    Arr.append(list(map(int, input().split())))

Arr = numpy.array(Arr)
print(numpy.transpose(Arr))
print(Arr.flatten())


