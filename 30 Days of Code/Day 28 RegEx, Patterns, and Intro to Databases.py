import re


List = []
for _ in range(int(input())):
    firstName, emailID = [str(s) for s in input().split()]
    if re.search('@gmail\.com$', emailID):
           List.append(firstName)
print(*sorted(List), sep='\n')
