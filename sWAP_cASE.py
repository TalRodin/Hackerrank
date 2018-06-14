def swap_case(s):
    list_=[]
    
    for i in s:
        if i.isalpha():
            if i.islower():
                u=i.upper()
                list_.append(u)
            elif i.isupper():
                l=i.lower()
                list_.append(l)
        elif i==' ':
            list_.append(i)
        elif i=='.':
            list_.append(i)
        elif i=="'":
            list_.append(i)
        elif i=='"':
            list_.append(i)
        elif i.isdigit():
            list_.append(i)
   
    
    return(''.join(list_))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)