#!/bin/python3

import os

def dynamicArray(n, queries):
    lastAnswer = 0
    Answer = []
    seqList = []
    countList = [0] * n
    for i in range(n):
        seqList.append([])
    
    for q, x, y in queries:
        # print(seqList)
        # print(countList)
        if q == 1:
            Pos = (x ^ lastAnswer) % n
            seqList[Pos].append(y)
            countList[Pos] += 1
        
        else:
            Pos = (x ^ lastAnswer) % n
            lastAnswer = seqList[Pos][y % countList[Pos]]
            Answer.append(lastAnswer)
    return Answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    result = dynamicArray(n, queries)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
