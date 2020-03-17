from itertools import product
K, M = map(int, input().split())
Ans = 0
Lists = []
for i in range(K):
    Lists.append([i * i for i in list(map(int, input().split()))[1 :]])

Max = 0
for i in product(*Lists):
    Max = max(Max, sum(i) % M)

print(Max)
