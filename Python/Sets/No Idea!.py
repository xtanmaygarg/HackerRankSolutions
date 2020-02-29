from collections import Counter
N, M = map(int, input().split())
Array = list(map(int, input().split()))
SetArray = set(Array)
A = set(map(int, input().split()))
B = set(map(int, input().split()))
Counts = Counter(Array)
S = 0
A = A.intersection(SetArray)
B = B.intersection(SetArray)
for i in A:
    S += Counts[i]
for i in B:
    S -= Counts[i]
print(S)
