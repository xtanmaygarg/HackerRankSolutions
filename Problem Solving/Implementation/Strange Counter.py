Curr = 3
T = int(input())

while(T > Curr):
    T -= Curr
    Curr *= 2

print(Curr - T + 1)
