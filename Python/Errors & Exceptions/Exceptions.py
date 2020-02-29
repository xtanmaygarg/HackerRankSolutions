for _ in range(int(input())):
    try:        
        a, b = map(int, input().split())
    except Exception as e:
        print("Error Code:", e)
        continue
    try:
        print(a // b)
    except Exception as e:
        print("Error Code:", e)
