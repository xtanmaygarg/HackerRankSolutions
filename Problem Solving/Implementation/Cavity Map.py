#!/bin/python3

import os

# Complete the cavityMap function below.
def cavityMap(grid):
    Ans = []
    for i in grid:
        Ans.append(i.copy())
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            X = int(grid[i][j])
            if X > max(int(grid[i + 1][j]), int(grid[i - 1][j]), int(grid[i][j + 1]), int(grid[i][j - 1])):
                Ans[i][j] = 'X'
    Result = []
    for i in Ans:
        Result.append("".join(i))
    return Result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = list(input())
        grid.append(grid_item)

    result = cavityMap(grid)


    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
