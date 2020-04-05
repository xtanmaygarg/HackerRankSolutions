import numpy
numpy.set_printoptions(legacy='1.13')

N, M = map(int,input().split())
Arr = numpy.array([input().split() for _ in range(M)],int)
print(numpy.mean(Arr,axis=1),numpy.var(Arr,axis=0),numpy.std(Arr), sep='\n')
