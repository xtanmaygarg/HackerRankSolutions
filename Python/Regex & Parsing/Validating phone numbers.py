import re
regex = r'[7-9][0-9]{9}$'
for _ in range(int(input())):
    Num = input()
    if re.match(regex, Num):
        print("YES")
    else:
        print("NO")
