import numpy
numpy.set_printoptions(legacy='1.13')
m=int(input())
list_=[]
for i in range(m):
    n=list(map(float, input().split()))
    list_.append(n)

my_array = numpy.array(list_)
print (numpy.linalg.det(my_array))
