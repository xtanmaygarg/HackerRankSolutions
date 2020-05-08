import os

def get_median(counts, mids):
    res = []
    for mid in mids:
        gone = 0
        for i, v in enumerate(counts):
            gone += v
            if gone >= mid:
                res.append(i)
                break
    return sum(res) / len(res)


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    alerts = 0
    counts = [0] * 201

    if d % 2 == 1:
        mids = [d // 2 + 1]
    else:
        mids = [d // 2, d // 2 + 1]

    for v in expenditure[:d]:
        counts[v] += 1

    for i, exp in enumerate(expenditure[d:]):
        median = get_median(counts, mids)

        if exp >= 2 * median:
            alerts += 1
        
        old_value = expenditure[i]
        counts[old_value] -= 1
        counts[exp] += 1
  
    return alerts
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
