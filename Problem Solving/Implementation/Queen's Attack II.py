#!/bin/python3

import os

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    obstacles = set(obstacles)
    Ans = 0
    Delta = [(0,1),(1,1),(1,0),(0,-1),(-1,-1),(-1,0),(1,-1),(-1,1)]

    for change in Delta:
        queenPos = [r_q, c_q]
        X = queenPos[0] + change[0]
        Y = queenPos[1] + change[1]
        while X >= 1 and X <= n and Y >= 1 and Y <= n:
            queenPos = (X, Y)
            if queenPos in obstacles:
                break
            Ans += 1
            X = queenPos[0] + change[0]
            Y = queenPos[1] + change[1]
    return Ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        A, B = map(int, input().rstrip().split())
        obstacles.append((A, B))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
