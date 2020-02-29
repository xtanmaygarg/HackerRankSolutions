#!/bin/python3

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    flag = 0
    for i in range(p,q+1):
        temp = str(i*i)
        d = len(str(i))
        r = int(temp[-d:len(temp)])
        if(len(temp)%2==0):
            l = int(temp[0:d])
        else:
            l = temp[0:d-1]
            if len(l)==0:
                l = 0
            else:
                l = int(l)
        if (r+l) == i:
            flag = 1
            print(i,end=' ')
    if(flag == 0):
        print("INVALID RANGE")

        

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
