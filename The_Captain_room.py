# Enter your code here. Read input from STDIN. Print output to STDOUT
def print_f(N,ls):
   print((sum(set(ls))*N-sum(ls))//(N-1))
if __name__=="__main__":
   N=int(input())
   ls=list(map(int, input().split()))
   print_f(N,ls)