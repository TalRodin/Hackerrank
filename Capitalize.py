# Complete the solve function below.
def solve(s):
    
    

    list_=[]
    m=s.split(' ')
    for i in m:
        list_.append(i)

    #print(list_)
    list_2=[]
    for i in list_:
        
        if i.isalpha():
            #print(i.title())
            list_2.append(i.title())
        else:
            list_2.append(i)
    return(' '.join(list_2))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
