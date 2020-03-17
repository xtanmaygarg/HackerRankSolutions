from itertools import combinations
from math import factorial

N = int(input())
Str = input().split()
K = int(input())

Total = factorial(N) // (factorial(K) * factorial(N - K))
Counter = 0
for i in combinations(Str, K):
    if 'a' in i:
        Counter += 1
print(Counter / Total)
