#program to demonstrate functionality of identity and eye functions of numpy module
import numpy
#print(numpy.identity(3))
#print(numpy.eye(8, 7, k = -1,dtype=numpy.int))
numpy.set_printoptions(legacy='1.13')
list1=input().strip().split()
tuple1=tuple([int(x) for x in list1])
print(numpy.eye(*tuple1,k=0))


