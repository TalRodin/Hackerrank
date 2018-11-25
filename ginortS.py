string_=list(input().strip())
#print(string_)
lower_case=[]
upper_case=[]
digits_odd=[]
digits_pos=[]
for i in string_:
    if i.isupper():
        upper_case.append(i)
    elif i.islower():
        lower_case.append(i)
    elif i in ['1','2','3','4','5','6','7','8','9','0']:
        if int(i)%2==0:
            digits_pos.append(int(i))
        else:
            digits_odd.append(int(i)) 
s_pos=sorted(digits_pos)
s_odd=sorted(digits_odd)
list_=sorted(lower_case)+sorted(upper_case)+[str(i) for i in s_odd]+[str(i) for i in s_pos]
for i in list_:
    print(*i, end='')