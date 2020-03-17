for _ in range(int(input())):
    N = input()
    try:
        X = float(N)
        if int(X) == X:
            if '.' in N:
                print(True)
            else:
                print(False)
        else:
            print(True)
    except Exception:
        print(False)
