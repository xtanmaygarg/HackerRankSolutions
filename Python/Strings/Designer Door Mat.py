n, m = map(int, input().split())
x = ".|."
y = "---"
# Upper Loop
o = n//2
p = 1
for j in range(n//2):
    print((y * o) + (x * p)+ (y * o))
    o -= 1
    p += 2
    
# Middle Loop
print("WELCOME".center(m, "-"))

# Lower Loop
p = n - 2
o = 1
for j in range(n//2):
    print((y * o) + (x * p)+ (y * o))
    o += 1
    p -= 2
