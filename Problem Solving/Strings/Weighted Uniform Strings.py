#!/bin/python3
import os

def weightedUniformStrings(s, queries):
    Dict = {}
    L = len(s)
    Result = []
    Weight = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,           'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,        's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

    Curr = s[0]
    CurrLen = 1
    Dict[Weight[Curr] * CurrLen] = True
    for i in range(1, L):
        if Curr == s[i]:
            CurrLen += 1
            Dict[Weight[Curr] * CurrLen] = True
        
        else:
            Curr = s[i]
            CurrLen = 1
            Dict[Weight[Curr] * CurrLen] = True
    for i in queries:
        try:
            if Dict[i]:
                Result.append('Yes')
        except Exception:
            Result.append('No')
    return Result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    queries_count = int(input())
    queries = []
    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)
    result = weightedUniformStrings(s, queries)
    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()
