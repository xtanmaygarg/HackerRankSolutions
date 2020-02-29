from collections import namedtuple
N = int(input())
Details = namedtuple('Details', input().split())
Su = 0
for i in range(N):
    A, B, C, D = input().split()
    Mark = Details(A, B, C, D)
    Su += int(Mark.MARKS)
print("%.2f" %(Su/N))
