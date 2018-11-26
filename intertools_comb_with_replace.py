from itertools import combinations_with_replacement
A=input().split()
for i in sorted([sorted(i) for i in list(combinations_with_replacement(A[0],int(A[1])))]):
    print(''.join(i))
