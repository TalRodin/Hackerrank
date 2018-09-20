from collections import namedtuple
n=int(input())
m=input().split()
x=m.index('MARKS')
print(x)      
Average=namedtuple('Average', m)
list_=[]
for i in range(n):
    marks=input().split()
    xyz=Average(marks[0],marks[1],marks[2],marks[3])
    
    list_.append(int(xyz[x]))

print(sum(list_)/len(list_))
