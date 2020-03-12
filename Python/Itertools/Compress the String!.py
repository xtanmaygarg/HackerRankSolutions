from itertools import groupby
print(*[(len(list(X)), int(Y)) for Y, X in groupby(input())])
