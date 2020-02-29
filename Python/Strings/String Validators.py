def aln(s):
    s = list(s)
    for i in s:
        if i.isalnum():
            return True
    return False
def al(s):
    s = list(s)
    for i in s:
        if i.isalpha():
            return True
    return False
def dig(s):
    s = list(s)
    for i in s:
        if i.isdigit():
            return True
    return False
def low(s):
    s = list(s)
    for i in s:
        if i.islower():
            return True
    return False
def upp(s):
    s = list(s)
    for i in s:
        if i.isupper():
            return True
    return False
if __name__ == '__main__':
    s = input()
    print(aln(s))
    print(al(s))
    print(dig(s))
    print(low(s))
    print(upp(s))


