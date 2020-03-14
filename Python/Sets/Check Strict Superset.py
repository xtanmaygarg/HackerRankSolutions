S = set(map(int, input().split()))
N = int(input())
Sets = []
for _ in range(N):
    Sets.append(set(map(int, input().split())))

flag = True
for i in Sets:
    if not S.issuperset(i):
        flag = False
        break
print(flag)
