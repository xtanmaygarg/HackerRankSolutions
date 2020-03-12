T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    i = 0
    j = N - 1
    Curr = 10e15
    flag = True
    while(i < j):
        if A[i] >= A[j] and Curr >= A[i]:
            Curr = A[i]
            i += 1
            
        elif A[j] > A[i] and Curr >= A[j]:
            Curr = A[j]
            j -= 1
        
        else:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")
            



