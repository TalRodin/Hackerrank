m=int(input())
l_1=set(input().split())
n=int(input())
l_2=set(input().split())

l=list(l_1.symmetric_difference(l_2))

print(l)
total=0
for i in l:
    total+=1
print(total)
