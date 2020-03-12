from itertools import combinations_with_replacement
In = input().split()
S = list(In[0])
S.sort()
S = "".join(S)
K = int(In[1])

for i in combinations_with_replacement(S, K):
    print("".join(i))
