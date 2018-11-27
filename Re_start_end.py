import re
S= input()
k= input()
if not re.search(k, S):
    print('(-1, -1)')
else:
    i = 0
    while re.search(k, S[i:]):
        i += re.search(k, S[i:]).start() + 1
        print('(', i-1, ', ', i+len(k)-2, ')', sep='')
