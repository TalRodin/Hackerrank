if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    count=0.0
    for key in student_marks:
        if key==query_name:
            count=sum((student_marks[key]))
            
    print(format(count/3, '.2f'))