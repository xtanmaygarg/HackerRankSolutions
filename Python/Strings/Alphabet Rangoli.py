import math
def print_rangoli(size):
    x = "--"
    d = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g',8:'h', 9:'i', 10:'j', 11:'k',            12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u',          22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}

    # Upper Loop
    upper  = n - 1
    alpha = 1
    while(upper > 0):
        i = alpha
        j = math.ceil(i/2)
        l = i - j
        k = n
        s = ""
        while(j > 0):
            s += d[k] + "-"
            k -= 1
            j -= 1
        k += 2
        while(l > 0):
            s += d[k] + "-"
            k += 1
            l -= 1
        s = s[:-1]
        print((x * upper) + s + (x * upper))
        upper -= 1
        alpha += 2

    # Middle Line
    alpha = n * 2 - 1
    i = alpha
    j = math.ceil(i/2)
    l = i - j
    k = n
    s = ""
    while(j > 0):
        s += d[k] + "-"
        k -= 1
        j -= 1
    k += 2
    while(l > 0):
        s += d[k] + "-"
        k += 1
        l -= 1
    s = s[:-1]
    print(s)
    
    # Lower Part
    upper = 1
    alpha = 2 * n - 3
    while(upper < n):
        i = alpha
        j = math.ceil(i/2)
        l = i - j
        k = n
        s = ""
        while(j > 0):
            s += d[k] + "-"
            k -= 1
            j -= 1
        k += 2
        while(l > 0):
            s += d[k] + "-"
            k += 1
            l -= 1
        s = s[:-1]
        print((x * upper) + s + (x * upper))
        upper += 1
        alpha -= 2

