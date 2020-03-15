from collections import defaultdict, Counter

def coverAll(Graph, i, Done):
    X = set()
    Stack = {i}
    while(Stack):
        Curr = Stack.pop()
        if Done[Curr]:
            continue
        else:
            Stack = Stack.union(Graph[Curr])
            Done[Curr] = True
            X.add(Curr)
    return X

def journeyToMoon(n, astronaut):
    Graph = defaultdict(set)
    Ans = []
    Final = 0
    Done = dict(zip(range(n), [False] * n))
    Fin = set(range(n))

    for i, j in astronaut:
        Graph[i].add(j)
        Graph[j].add(i)

    while(Fin):
        i = Fin.pop()
        Fin.add(i)
        X = coverAll(Graph, i, Done)
        L = len(X)
        Ans.append(L)
        Fin.difference_update(X)
    C = Counter(Ans)
    Final = 0
    X = list(C.keys())
    L1 = len(X)
    for i in range(L1):
        if C[X[i]] > 1:
            Final += X[i] * X[i] * ((C[X[i]] * (C[X[i]] - 1)) // 2)
        for j in range(i + 1, L1):
            Final += X[i] * X[j] * C[X[i]] * C[X[j]]
    return Final

n, p = map(int, input().split())
astronaut = []
for _ in range(p):
    astronaut.append(list(map(int, input().rstrip().split())))
result = journeyToMoon(n, astronaut)
print(result)
