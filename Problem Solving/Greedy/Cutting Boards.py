for _ in range(int(input())):
    N, M = map(int, input().split())
    Cost_1 = list(map(int, input().split()))
    Cost_2 = list(map(int, input().split()))
    NY = {}
    MY = {}
    Cut_X = 1
    Cut_Y = 1

    for i in Cost_2:
        try:
            if NY[i]:
                NY[i] += 1
        except Exception:
            NY[i] = 1

    for i in Cost_1:
        try:
            if MY[i]:
                MY[i] += 1
        except Exception:
            MY[i] = 1

    Cost = Cost_1 + Cost_2
    Cost.sort(reverse = True)
    Final = 0

    for i in Cost:
        F = 0
        try:
            if MY[i]:
                F += 1
        except Exception:
            pass
        try:
            if NY[i]:
                F += 2
        except Exception:
            pass

        if F == 1:
            Final += i * Cut_Y
            MY[i] -= 1
            Cut_X += 1

        elif F == 2:
            Final += i * Cut_X
            NY[i] -= 1
            Cut_Y += 1
            
        else:
            if Cut_X >= Cut_Y:
                Final += i * Cut_Y
                MY[i] -= 1
                Cut_X += 1
            
            else:
                Final += i * Cut_X
                NY[i] -= 1
                Cut_Y += 1
    print(Final % 1000000007)
