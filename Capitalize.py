def solve(s):
    m=s.split(' ')
    list_=[]
    for i in m:       
        if i.isalpha():
            list_.append(i.title())
        else:
            list_.append(i)
    return(' '.join(list_))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
