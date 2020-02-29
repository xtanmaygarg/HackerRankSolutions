import math

def encryption(s):
    L = len(s)
    R = math.floor(L ** 0.5)
    C = math.ceil(L ** 0.5)
    if R * C < L:
        R = C
    Ans = []
    for i in range(C):
        Ans.append(s[i::C])
    Ans = " ".join(Ans)
    return Ans

if __name__ == '__main__':
    s = input().strip()
    result = encryption(s)
    print(result)
