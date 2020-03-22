#!/bin/python3

import os

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    Ans = ''
    k = k % 26
    for i in s:
        if i.isalpha():
            if i.islower():
                if (ord(i) + k) > 122:
                    Ans += chr(96 + (ord(i) + k) % 122)
                else:
                    Ans += chr(ord(i) + k)
            else:
                if (ord(i) + k) > 90:
                    Ans += chr(64 + (ord(i) + k) % 90)
                else:
                    Ans += chr(ord(i) + k)
        else:
            Ans += i
    return Ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
