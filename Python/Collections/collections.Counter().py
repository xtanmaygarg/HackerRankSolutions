from collections import Counter
x = int(input())
avail = list(map(int, input().split()))
count = dict(Counter(avail))
n = int(input())
total = 0
for i in range(n):
    size, cost = map(int, input().split())
    if size not in count.keys():
        continue
    if count[size] > 0:
        total += cost
        count[size] -= 1
print(total)
