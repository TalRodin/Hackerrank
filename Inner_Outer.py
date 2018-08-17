import numpy
n=list(map(int, input().split()))
m=list(map(int, input().split()))
A = numpy.array(n)
B = numpy.array(m)
print (numpy.inner(A, B))
print (numpy.outer(A, B))


