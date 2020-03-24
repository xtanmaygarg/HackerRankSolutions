import re
import email.utils as E

def check(s):
    return re.match(r'[a-zA-Z][a-zA-Z0-9-_\.]+@[a-zA-Z]+\.[a-zA-Z]{0,3}$',s)

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        Name, Email = E.parseaddr(input())
        if check(Email):
            print(E.formataddr((Name, Email)))
