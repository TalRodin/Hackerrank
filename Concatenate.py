import numpy

arr = map(int, input().split())
l=list(arr)
N = numpy.array([input().split() for i in range(l[0])], int)
M = numpy.array([input().split() for i in range(l[1])], int)

print (numpy.concatenate((N, M), axis = 0))
