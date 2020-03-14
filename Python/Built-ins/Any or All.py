N = int(input())
L = list(map(int, input().split()))
print(any(str(i) == str(i)[::-1] for i in L) and all(i >= 0 for i in L))
