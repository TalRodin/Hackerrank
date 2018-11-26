# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
def f(purchase,size):
    total=0
    for i in range(purchase):
        j=list(map(int, input().split()))
        if j[0] in Counter(size).keys():
            total+=j[1]
            size.remove(j[0])

    print(total)

if __name__=='__main__':
    N=int(input())
    size=list(map(int, input().split()))
    purchase= int(input())
    f(purchase,size)
