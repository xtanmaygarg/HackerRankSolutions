#!/bin/python3

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    Dict = {}
    N = len(cost)
    for i in range(N):
        try:
            if Dict[money - cost[i]]:
                print(Dict[money - cost[i]], i + 1)
                break
        except Exception:
            Dict[cost[i]] = i + 1

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
