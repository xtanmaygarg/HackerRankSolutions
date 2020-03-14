N = int(input())
S = set(map(int, input().split()))
O = int(input())
for _ in range(O):
    Op, L = input().split()
    T = set(map(int, input().split()))
    if Op == 'intersection_update':
        S.intersection_update(T)
    elif Op == 'update':
        S.update(T)
    elif Op == 'symmetric_difference_update':
        S.symmetric_difference_update(T)
    else:
        S.difference_update(T)
print(sum(S))
