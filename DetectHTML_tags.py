# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/env python3
from html.parser import HTMLParser

class parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for x, y in attrs:
            print("-> {} > {}".format(x, y))

if __name__ == '__main__':
    p = parser()
    for _ in range(int(input())):
        p.feed(input())