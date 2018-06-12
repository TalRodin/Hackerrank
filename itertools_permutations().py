#itertools.permutations()
from itertools import permutations
string_, num = input().split(' ')
l=list(permutations(string_,int(num)))
list_=[]
for i in l:
    list_.append(''.join(i))
#print(sorted(list_))
for i in sorted(list_):
    print(i)
