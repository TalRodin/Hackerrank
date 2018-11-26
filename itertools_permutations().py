from itertools import permutations
n=input().split()
for i in sorted(list(permutations(n[0],int(n[1])))):
    print(''.join(i))
