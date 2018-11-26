# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=map(int,input().split())
print(any(str(i)==str(i)[::-1] for i in l ) and all(i>0 for i in l))