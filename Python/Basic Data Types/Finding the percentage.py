if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    lis = student_marks[query_name]
    val = round(sum(lis)/len(lis), 2)
    print("%.2f"%val)

