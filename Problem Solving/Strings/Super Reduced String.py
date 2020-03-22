#!/bin/python3

import os

def superReducedString(s):    
    while(True):
        L = len(s)
        Ans = ''
        if not s:
            return "Empty String"
        Curr = s[0]
        Val = 1
        for i in range(1, L):
            if s[i] == Curr:
                Val += 1
            
            else:
                if Val & 1:
                    Ans += Curr
                Curr = s[i]
                Val = 1
        if Val & 1:
            Ans += Curr
        if Ans == s:
            if Ans:
                return Ans
            else:
                return "Empty String"
        else:
            s = Ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = superReducedString(s)
    fptr.write(result + '\n')
    fptr.close()
