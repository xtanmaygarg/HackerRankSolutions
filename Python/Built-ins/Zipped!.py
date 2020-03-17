N, X = map(int, input().split())
Marks = []
for _ in range(X):
    Marks.append(list(map(float, input().split())))

for i in zip(*Marks):
    print(sum(i) / X)
