if __name__ == '__main__':
    S = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score not in S.keys():
            S[score] = [name]
        else:
            S[score].append(name)
    num = sorted(S.keys())[1]
    val = sorted(S[num])
    for i in val:
        print(i)
