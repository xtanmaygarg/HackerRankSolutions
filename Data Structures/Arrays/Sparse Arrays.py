#!/bin/python3

import os
from collections import Counter

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    Count = Counter(strings)
    Ans = []
    for i in queries:
        try:
            Ans.append(Count[i])
        except Exception:
            Ans.append(0)
    
    return Ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
