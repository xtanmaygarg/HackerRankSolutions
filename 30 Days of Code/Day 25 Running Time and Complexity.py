def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for x in range(2, int((num**0.5)) + 1):
        if num % x == 0:
            return False
    return True
for _ in range(int(input())):
    N = int(input())
    if is_prime(N):
        print("Prime")
    else:
        print("Not prime")
