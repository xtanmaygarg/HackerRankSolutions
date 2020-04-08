N = int(input())
Stack = []
SupportingStack = []
for _ in range(N):
    Type = input().split()
    if Type[0] == '1':
        Stack.append(int(Type[1]))
        if SupportingStack:
            if SupportingStack[-1] <= int(Type[1]):
                SupportingStack.append(int(Type[1]))

        else:
            SupportingStack.append(int(Type[1]))
    
    elif Type[0] == '2':
        Num = Stack.pop()
        if Num == SupportingStack[-1]:
            SupportingStack.pop()
    else:
        print(SupportingStack[-1])
