from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        for arg0, arg1 in attrs:
            print('->', arg0, '>', arg1)
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for arg0, arg1 in attrs:
            print('->', arg0, '>', arg1)



n=int(input())
string_=''
for i in range(n) :
    string_+=input()
print(string_)

parser = MyHTMLParser()
parser.feed(string_)