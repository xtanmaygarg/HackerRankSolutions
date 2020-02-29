if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    maximum = max(arr)
    while maximum in arr:
        arr.remove(maximum)
    result = max(arr)
    print(result)

