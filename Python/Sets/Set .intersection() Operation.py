N = int(input())
E = set(map(int, input().split()))
M = int(input())
F = set(map(int, input().split()))
print(len(E.intersection(F)))
