#!/bin/python3

import os

def winningLotteryTicket(tickets):
    Mapping = [0] * 1024
    Answer = 0
    for ticket in tickets:
        Val = 0
        for num in ticket:
            Val += (2 ** int(num))
        Mapping[Val] += 1
    for i in range(1024):
        for j in range(i + 1, 1024):
            if i | j == 1023:
                Answer += (Mapping[i] * Mapping[j])
    Answer += (Mapping[1023] * (Mapping[1023] - 1)) // 2
    return Answer



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    tickets = []
    for _ in range(n):
        tickets_item = set(input())
        tickets.append(tickets_item)

    result = winningLotteryTicket(tickets)

    fptr.write(str(result) + '\n')
    fptr.close()
