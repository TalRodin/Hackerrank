from itertools import combinations_with_replacement

A=input().split()
n=combinations_with_replacement(A[0],int(A[1]))
list_1=[]
for i in n:
    j=sorted(i)
    list_1+=[''.join(j)]   
#print(list_1)    
for i in sorted(list_1):
    print(i)
