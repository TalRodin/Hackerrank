from collections import defaultdict
n,m=input().split(' ')
d = defaultdict(list)
for i in range(int(n)):
    d[input()].append(i+1)  
list_=[input() for i in range(int(m))]

for i in list_:
    if i in d:
        print (' '.join(map(str, d[i])))
    else:
        print('-1') 
        
