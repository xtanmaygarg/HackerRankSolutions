import re

S = input()
X = re.findall(r'([a-zA-Z0-9])\1+', S)
if X:
    print(X[0])
else:
    print(-1)
