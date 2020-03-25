#!/bin/python3

import sys

def separateNumbers(s):
    if s[0] == s:
        print('NO')
        return
    for i in range(1, len(s)):
        Stack = []
        Stack.append(s[:i])
        while len(''.join(Stack)) < len(s):
            Stack.append(str(int(Stack[-1]) + 1))
        if ''.join(Stack) == s:
            print('YES', Stack[0])
            break
        if i == len(s) - 1:
            print('NO')

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        separateNumbers(s)
