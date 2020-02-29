from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(list)
for t in range(n):
    word = input()
    d[word].append(t + 1)
for _ in range(m):
    word = input()
    if len(d[word]) > 0:
        print(*d[word])
    else:
        print(-1)
