a=float(input())
b=float(input())
q=a/b
q=str(q).split('.')

#print(q)

print(int(a//b))
print(int(a%b))
l=[]
l.append(int(a//b))
l.append(int(a%b))
l_2=[]
for i in l:
    l_2.append(str(i))
print('('+l_2[0]+', '+l_2[1]+')')