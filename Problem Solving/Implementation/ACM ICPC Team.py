#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    Max = 0
    Count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            New = str(topic[i] + topic[j]).count('1') + str(topic[i] + topic[j]).count('2')
            if New == Max:
                Count += 1
            elif New > Max:
                Max = New
                Count = 1
    return Max, Count




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(int(topic_item))

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
