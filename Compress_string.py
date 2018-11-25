from itertools import groupby
string_=list(map(int,input()))
n=[(len(list(g)),k) for k, g in groupby(string_)]
for i in n:
    print(i, end=' ')