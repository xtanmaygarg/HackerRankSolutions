import os

# Complete the gemstones function below.
def gemstones(arr):
    Set = set(arr[0])
    for i in arr:
        Set.intersection_update(set(i))
    return len(Set)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
