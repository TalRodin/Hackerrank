import re

string_ = input()
m = re.search(r"([a-z0-9A-Z])\1+", string_)
if m:
    print(m.group(1))
else:
    print("-1")
