import numpy

m=list(map(int, input().split()))
list_=[]
for i in range(m[0]):
    n=list(map(int, input().split()))
    list_.append(n)
#print numpy.sum(my_array, axis = 0) 
my_array = numpy.array(list_)

#print (numpy.sum(my_array, axis = 0)  )
print (numpy.prod(numpy.sum(my_array, axis = 0)) )
