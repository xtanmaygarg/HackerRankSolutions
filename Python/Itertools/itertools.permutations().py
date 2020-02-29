from itertools import permutations
string, k = input().split()
k = int(k)
permutation = list(permutations(string, k))
permutation.sort()
for i in permutation:
    print("".join(list(i)))
