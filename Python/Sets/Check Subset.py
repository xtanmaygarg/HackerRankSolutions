for _ in range(int(input())):
    N = int(input())
    S = set(map(int, input().split()))
    M = int(input())
    T = set(map(int, input().split()))
    if S.issubset(T):
        print("True")
    else:
        print("False")
