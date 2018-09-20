n=int(input())
N=set(map(int, input().split()))
m=int(input())
M=set(map(int, input().split()))
X=N.symmetric_difference(M)
X=sorted(X)
for i in X:
    print(i)