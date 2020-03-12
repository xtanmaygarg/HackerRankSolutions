from itertools import combinations
S, k = input().split()
k = int(k)
S = sorted(S)

for i in range(1, k + 1):
    Com = list(combinations(S, i))
    for j in Com:
        print("".join(j))
