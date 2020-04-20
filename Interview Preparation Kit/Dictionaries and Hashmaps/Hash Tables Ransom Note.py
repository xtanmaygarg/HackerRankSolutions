#!/bin/python3

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    Hash = {}
    for word in magazine:
        try:
            Hash[word] += 1
        except Exception:
            Hash[word] = 1
    
    for word in note:
        try:
            Hash[word] -= 1
            if Hash[word] == -1:
                return "No"
        except Exception:
            return "No"
    return "Yes"


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
