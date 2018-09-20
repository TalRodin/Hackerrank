list_ = []
n=int(input())
for i in range(n):
    x=input()
    list_.append(str(x))

for j in list_:
    l= list(j)
    if (l[0] =='7' or l[0] =='8' or l[0] =='9') and len(l)==10 and (j.isdigit()==True):
        print("YES")
    else:
        print("NO")
