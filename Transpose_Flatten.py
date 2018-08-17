import numpy

arr=list(map(int, input().split()))
l=[list(map(int, input().split())) for i in range(arr[0])]

my_array = numpy.array(l)
print(numpy.transpose(my_array))
print (my_array.flatten())