from collections import Counter
K = int(input())
M = list(map(int, input().split()))
C = Counter(M)
MC = C.most_common()
print(MC[-1][0])
