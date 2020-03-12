n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    Act = input().split()
    if Act[0] == 'pop':
        try:
            s.pop()
        except Exception:
            pass

    elif Act[0] == 'remove':
        try:
            s.remove(int(Act[1]))
        except Exception:
            pass

    else:
        s.discard(int(Act[1]))
print(sum(s))
