#!/bin/python3
import os

# Complete the climbingLeaderboard function below.

def binarySearch(arr, l, r, x):
    while l <= r:
        mid = (l + r) // 2
        # Check if x is present at mid
        if mid == 0:
            if arr[mid] == x:
                return 1
            elif arr[mid] < x:
                return 1
            else:
                return 2
            
        elif arr[mid] == x:
            return mid + 1
  
        elif arr[mid] > x:
            if mid == r - 1:
                return r + 1
            elif arr[mid + 1] < x:
                return mid + 2
            else:
                l = mid + 1
        else:
            if arr[mid - 1] == x:
                return mid
            elif arr[mid - 1] > x:
                return mid + 1
            else:
                r = mid - 1

def climbingLeaderboard(scores, alice):
    scores = list(set(scores))
    scores.sort(reverse = True)
    N = len(scores)
    Ans = []
    for points in alice:
        Ans.append(binarySearch(scores, 0, N, points))
    return Ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
