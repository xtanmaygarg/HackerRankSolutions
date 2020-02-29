#!/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
if(N%2!=0):
    print("Weird");
elif(N>1 and N<6 and N&2==0):
    print("Not Weird");
elif(N<21):
    print("Weird");
elif(N>21 and N%2==0):
    print("Not Weird");


