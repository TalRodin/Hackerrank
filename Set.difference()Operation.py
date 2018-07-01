a=int(input())
e=input().split(' ')

s_1=set(e)
b=int(input())
e_2=input().split(' ')
s_2=set(e_2)
#print(set(e))
#print(set(e_2))
count=s_1-s_2
total=0
for i in count:
    total+=1
print(total)