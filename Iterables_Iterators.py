import itertools
N=int(input())
string_=list(map(str, input().split()))
x=int(input())
list_=[_ for _ in itertools.combinations(string_, x)]
length=len(list_)
total=0
for i in list_:
    if 'a' in i:
        total+=1
print(round(total/length,3))
