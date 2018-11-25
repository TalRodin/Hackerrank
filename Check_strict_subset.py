A=set(input().split(' '))
n=input()
list_=[]
for i in range(int(n)):
    sub_set=set(input().split(' '))     
    if not A>sub_set or len(A)<=len(sub_set):
        list_.append(False)
    else:
        list_.append(True)
if False in list_:
    print(False)
else:
    print(True)