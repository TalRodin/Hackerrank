from itertools import combinations

A=input().split()
a = sorted(A[0])
n = int(A[1])


for i in range(1, n+1):
    l = map("".join, list(combinations(a, i)))

    for j in sorted(l):
        print (j)
        
        
