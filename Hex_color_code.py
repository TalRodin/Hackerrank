import re
n=int(input())
print(n)
for i in range(n):
    m = re.findall(r'#[0-9a-fA-F]{3,6}', input()[1:])
    print(m)
    if len(m):
        print(*m, sep = '\n')
