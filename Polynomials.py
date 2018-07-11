import numpy
array = map(float, input().split())
n=input()
print (numpy.polyval(list(array), float(n)))