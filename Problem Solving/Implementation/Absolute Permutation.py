T = int(input())
for _ in range(T):
    N, k = map(int, input().split())
    Dict = dict()
    for i in range(1, N + 1):
        Dict[i] = 1

    Permutation = []
    Done = False
    for i in range(1, N + 1):
        if i > k:
            Do = True
            Poss1 = i + k
            Poss2 = i - k
            try:
                if Dict[Poss2]:
                    Do = False
                    Permutation.append(Poss2)
                    Dict[Poss2] -= 1
            except Exception:
                pass
            if Do:
                try:
                    if Dict[Poss1]:
                        Permutation.append(Poss1)
                        Dict[Poss1] -= 1
                except Exception:
                    print(-1)
                    Done = True
                    break
            else:
                pass
                        
        else:
            Poss = i + k
            try:
                if Dict[Poss]:
                    Permutation.append(Poss)
                    Dict[Poss] -= 1
            except Exception:
                print(-1)
                Done = True
                break
    if Done:
        continue
    else:
        print(*Permutation)
