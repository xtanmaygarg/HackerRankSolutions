#!/bin/python3
import os

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    Cond = 4
    numFlag = True
    lowFlag = True
    upFlag = True
    speChar = True
    for i in password:
        print(i, Cond)
        if Cond:
            if i in numbers and numFlag:
                Cond -= 1
                numFlag = False
            elif i in lower_case and lowFlag:
                Cond -= 1
                lowFlag = False
            elif i in upper_case and upFlag:
                Cond -= 1
                upFlag = False
            elif i in special_characters and speChar:
                Cond -= 1
                speChar = False
        else:
            break
    return max(Cond, 6 - n)





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    password = input()
    answer = minimumNumber(n, password)
    fptr.write(str(answer) + '\n')
    fptr.close()
