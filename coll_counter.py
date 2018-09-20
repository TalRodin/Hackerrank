from collections import Counter
n=int(input())
l=list(map(int, input().split()))
m=int(input())
total=0
list_=[]
for i in range(m):    
    p=list(map(int, input().split()))
    if p[0] in l:

          list_.append(p[1])
          l.remove(p[0])
          
print(sum(list_))