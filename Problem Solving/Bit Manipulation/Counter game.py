#!/bin/python

import os

# Complete the counterGame function below.
def counterGame(n):
    Count = 0
    while(n > 1):
        N = bin(n)
        if N.count('1') == 1:
            n = n // 2
        else:
            n = n - 2 ** (len(N) - 3)
        Count += 1
    if Count % 2:
        return "Louise"
    else:
        return "Richard"




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
