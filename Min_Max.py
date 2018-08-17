import numpy
m=list(map(int, input().split()))
list_=[]
for i in range(m[0]):
    n=list(map(int, input().split()))
    list_.append(n)
my_array = numpy.array(list_)
#print (numpy.min(my_array, axis = 1))
print( numpy.max(numpy.min(my_array, axis = 1)) )