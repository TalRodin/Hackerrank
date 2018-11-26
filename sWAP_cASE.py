def swap_case(s):
    list_=[]
    for i in s:
        if i.isalpha():
            if i.isupper():
                list_.append(i.lower())
            else:
                list_.append(i.upper())
        elif i.isdigit():
            list_.append(i)
        elif i=='.':
            list_.append(i)
        elif i=='"':
            list_.append(i)
        elif i==' ':
            list_.append(i)
        elif i=="'":
            list_.append(i)
        
    return(''.join(list_))


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
