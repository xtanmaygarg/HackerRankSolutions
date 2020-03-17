import re
for _ in range(int(input())):
    S = input()
    try:
        re.compile(S)
        print(True)
    except:
        print(False)
