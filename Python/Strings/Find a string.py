def count_substring(string, sub_string):
    i = 0
    val = 0
    while(i < len(string) - len(sub_string) + 1):
        if sub_string == string[i: i+len(sub_string)]:
            val += 1
        i += 1
    return val

