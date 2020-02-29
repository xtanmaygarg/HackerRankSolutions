from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))
final = list(product(a,b))
for i in final:
    print(i, end = " ")

