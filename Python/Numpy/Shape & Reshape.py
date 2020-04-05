import numpy

Arr = list(map(int, input().split()))
Arr = numpy.array(Arr)
Arr.shape = (3, 3)
print(Arr)
