import numpy
N, M = map(int, input().split())
numpy.set_printoptions(legacy='1.13')
print(numpy.eye(N, M))
