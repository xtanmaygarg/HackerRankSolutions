from collections import defaultdict

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

def roadsAndLibraries(n, c_lib, c_road, cities):
    Graph = defaultdict(set)
    Ans = 0
    Done = dict(zip(range(1, n + 1), [False] * n))
    Fin = set(range(1, n + 1))

    for i, j in cities:
        Graph[i].add(j)
        Graph[j].add(i)

    while(Fin):
        i = Fin.pop()
        Fin.add(i)
        X = coverAll(Graph, i, Done)
        L = len(X)
        if L == 1:
            Ans += c_lib
        else:
            Ans += min((L - 1) * c_road + c_lib, L * c_lib)
        Fin.difference_update(X)
    return Ans

q = int(input())
for q_itr in range(q):
    n, m, c_lib, c_road = map(int, input().split())
    cities = []
    for _ in range(m):
        cities.append(list(map(int, input().rstrip().split())))

    result = roadsAndLibraries(n, c_lib, c_road, cities)
    print(result)
