from collections import defaultdict
n,m=input().split(' ')
d = defaultdict(list)
list_=[]

for i in range(int(n)):
    d[input()].append(i+1)  
 
for i in range(int(m)):
    list_.append(input())

for i in list_:
    if i in d:
        print (' '.join(map(str, d[i])))
    else:
        print('-1') 
        