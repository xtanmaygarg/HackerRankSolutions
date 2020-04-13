#!/bin/python3

import os

# Complete the gridSearch function below.
def gridSearch(G, P):
    for i in range(R-r+1):
        for j in range(C-c+1):
            Flag = True
            for k in range(r):
                if P[k] != G[i+k][j:j+c]:
                    Flag = False
                    break
            if Flag:
                return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
