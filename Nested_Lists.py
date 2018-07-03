if __name__ == '__main__':
    dict_={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dict_[name]=score
    #print(dict_)
    student=list(dict_)
    #print(student)
    list_=[]
    for i in dict_:
        list_.append(dict_[i])
    #print(list_)
    l=sorted(set(list_))
    #print(l)
    list_names=[]
    for i in dict_:
        if dict_[i]==l[1]:
            list_names.append(i)
    #print(list_names)
    s=sorted(list_names)
    for i in s:
        print(i)



