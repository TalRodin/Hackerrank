def f(student_marks, query_name):
    print(format((sum(student_marks[query_name])/len(student_marks[query_name])),'.2f'))
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    f(student_marks, query_name)
