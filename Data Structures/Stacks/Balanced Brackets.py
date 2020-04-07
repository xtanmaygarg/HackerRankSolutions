#!/bin/python3

import os

# Complete the isBalanced function below.
def isBalanced(In):
    Len = len(In)
    Stack = []
    j = 0
    for i in range(Len):
        if In[i] == '[' or In[i] == '{' or In[i] == '(':
            Stack.append(In[i])
        else:
            if len(Stack) == 0:
                break
            elif (Stack[-1] + In[i]) in ["[]", "{}", "()"]:
                Stack.pop()
            else:
                break
        j += 1
    if i != Len - 1 or Stack:
        return "NO"
    else:
        return "YES"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
