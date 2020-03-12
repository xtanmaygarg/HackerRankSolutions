N = int(input())
E = set(map(int, input().split()))
B = int(input())
F = set(map(int, input().split()))

S = E.union(F)
print(len(S))
