#!/bin/python3

inputs = input()
n = int(input())
if inputs == 'a':
    print(n)
else:
    value = inputs.count('a')
    count1 = value * (n//len(inputs))
    cutoff = n%len(inputs)
    strings = inputs[0:cutoff]
    count2 = strings.count('a')
    count = count1 + count2
    print(count)
    
