import numpy

n=int(input())
list_1=[]
for i in range(n):
    m=list(map(int, input().split()))
    list_1.append(m)
list_2=[]
for i in range(n):
    m=list(map(int, input().split()))
    list_2.append(m)
A=numpy.array(list_1)  
B=numpy.array(list_2)  
print (numpy.dot(A, B))
