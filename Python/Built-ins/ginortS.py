S = input()
L = ''
U = ''
OD = ''
ED = ''
for i in S:
    if i.islower():
        L += i
    elif i.isupper():
        U += i
    elif i.isdigit:
        if int(i) & 1:
            OD += i
        else:
            ED += i

print(''.join(sorted(L) + sorted(U) + sorted(OD) + sorted(ED)))
