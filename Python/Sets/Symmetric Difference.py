N = int(input())
S1 = set(map(int, input().split()))
M = int(input())
S2 = set(map(int, input().split()))

S = list(S1.symmetric_difference(S2))
S.sort()
for i in S:
    print(i)
