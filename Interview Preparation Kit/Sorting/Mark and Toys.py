#!/bin/python3

import os

def maximumToys(prices, k):
    Count = 0
    prices.sort()
    for price in prices:
        k -= price
        if k <= 0:
            return Count
        Count += 1



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
