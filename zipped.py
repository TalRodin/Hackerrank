n=list(map(int, input().split()))
list_=[]
for i in range(n[1]):

    line=list(map(float, input().split() ))
    list_.append(line)
print(list_)

M=zip(*list_)
print(M)
for i in M:
    print(sum(i)/len(i))