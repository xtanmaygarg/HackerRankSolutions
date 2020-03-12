from collections import Counter
if __name__ == '__main__':
    s = list(input())
    s.sort()
    s = "".join(s)
    C = Counter(s)
    M = C.most_common()
    M = M[:3]
    for i, j in M:
        print(i, j)

