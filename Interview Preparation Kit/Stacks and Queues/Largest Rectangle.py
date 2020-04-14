#!/bin/python3

import os

def Left_Smallest(N, Array):
    Output = []
    Stack = []
    for Index in range(N):
        if Stack:
            while(True):
                if Stack == []:
                    Output.append(-1)
                    Stack.append([Array[Index], Index])
                    break

                elif Stack[-1][0] < Array[Index]:
                    Output.append(Stack[-1][1])
                    Stack.append([Array[Index], Index])
                    break

                else:
                    Stack.pop()
                    
        else:
            Output.append(-1)
            Stack.append([Array[Index], Index])
    return Output

def Right_Smallest(N, Array):
    Output = []
    Stack = []
    for Index in range(N - 1, -1, -1):
        if Stack:
            while(True):
                if Stack == []:
                    Output.append(N)
                    Stack.append([Array[Index], Index])
                    break

                elif Stack[-1][0] < Array[Index]:
                    Output.append(Stack[-1][1])
                    Stack.append([Array[Index], Index])
                    break

                else:
                    Stack.pop()
                    
        else:
            Output.append(N)
            Stack.append([Array[Index], Index])
    return Output[:: -1]

def MAH(Array, N):
    Output = []
    Max = 0
    Left = Left_Smallest(N, Array)
    Right = Right_Smallest(N, Array)

    for i in range(N):
        Output.append((Right[i] - Left[i] - 1) * Array[i])
        Max = max(Max, Output[i])
    return Max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = MAH(h, n)

    fptr.write(str(result) + '\n')

    fptr.close()
