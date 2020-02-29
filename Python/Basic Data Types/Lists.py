if __name__ == '__main__':
    l = []
    N = int(input())
    for i in range(N):
        inp = input()
        if len(inp) <= 7:
            if inp == "print":
                print(l)
            elif inp == "sort":
                l.sort()
            elif inp == "reverse":
                l.reverse()
            elif inp == "pop":
                l.pop()
        else:       
            name, *line = inp.split()
            if name == "append":
                l.append(int(line[0]))
            elif name == "remove":
                l.remove(int(line[0]))
            elif name == "insert":
                l.insert(int(line[0]), int(line[1]))

