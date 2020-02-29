def merge_the_tools(string, k):
    n = len(string)
    i = 0
    while(i < n):
        s = string[i:i+k]
        t = ""
        for val in s:
            if val in t:
                continue
            else:
                t += val
        print(t)
        i += k
        
