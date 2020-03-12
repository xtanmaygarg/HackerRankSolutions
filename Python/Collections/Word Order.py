from collections import defaultdict

D = defaultdict()
for i in range(int(input())):
    Word = input()
    try:
        D[Word] += 1
    except Exception:
        D[Word] = 1
print(len(D))
for i in D:
    print(D[i],  end = " ")
