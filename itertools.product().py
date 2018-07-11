from itertools import product
arr=map(int, input().split())
arr2=map(int, input().split())
list_=list(product(arr,arr2))
for i in list_:
    print(i, end=' ')