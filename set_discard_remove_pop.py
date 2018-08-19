n = int(input())
s = set(map(int, input().split()))
i=int(input())
for j in range(i):
    m=input().split()
    if m[0]=='pop':
        s.pop()
    elif m[0]=='remove':
        s.remove(int(m[1]))
    elif m[0]=='discard':
        s.discard(int(m[1]))
print(sum(s))    
        