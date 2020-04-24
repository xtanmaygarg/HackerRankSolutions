#!/bin/python3

import os

def alternate(s):
    S = len(s)
    List = list(set(s))
    Max = 0
    L = len(List)
    for i in range(L):
        for j in range(i + 1, L):
            Flag = -1
            Curr = 0
            for k in range(S):
                if s[k] == List[i]:
                    if Flag == 0:
                        Curr = 0
                        break
                    else:
                        Curr += 1
                        Flag = 0
                elif s[k] == List[j]:
                    if Flag == 1:
                        Curr = 0
                        break
                    else:
                        Curr += 1
                        Flag = 1
                else:
                    pass
            Max = max(Max, Curr)
    return Max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    l = int(input().strip())
    s = input()
    result = alternate(s)
    fptr.write(str(result) + '\n')
    fptr.close()
