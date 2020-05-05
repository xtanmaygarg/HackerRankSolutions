# Run This Program in PYPY3
#!/bin/python3

import os

def freqQuery(queries):
    Mapping = {}
    Result = []
    for queryType, Val in queries:
        if queryType == 1:
            if Val in Mapping:
                Mapping[Val] += 1
            else:
                Mapping[Val] = 1

        elif queryType == 2:
            if Val in Mapping and Mapping[Val] != 0:
                Mapping[Val] -= 1

        else:
            if Val in Mapping.values():
                Result.append(1)
            else:
                Result.append(0)
    return Result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
