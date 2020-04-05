import numpy

N, M = map(int, input().split())
print(numpy.array([input().split() for _ in range(int(N))], int).min(1).max())
