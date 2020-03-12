from collections import deque

D = deque()
N = int(input())
for _ in range(N):
    In = input().split()
    A = In[0]
    if A == 'append':
        B = int(In[1])
        D.append(B)

    elif A == 'appendleft':
        B = int(In[1])
        D.appendleft(B)

    elif A == 'pop':
        try:
            D.pop()
        except Exception:
            pass
    else:
        try:
            D.popleft()
        except Exception:
            pass
print(*D)
