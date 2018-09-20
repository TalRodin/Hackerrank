from collections import OrderedDict
N=int(input())
ordered_dictionary = OrderedDict()
for i in range(N):
    l=input().rsplit(' ',1)
    if l[0] not in ordered_dictionary:
        ordered_dictionary[l[0]] =int(l[1])
    else:
       ordered_dictionary[l[0]] =ordered_dictionary[l[0]]+int(l[1] )
print(ordered_dictionary)

for i in ordered_dictionary.items():
    print (*i)

