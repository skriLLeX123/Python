#program to demonstrate functionality of zeros and ones functions of numpy module
import numpy
list1=input().strip().split()
tuple1=tuple([int(x) for x in list1])
print(numpy.zeros(tuple1,dtype=numpy.int))
print(numpy.ones(tuple1,dtype=numpy.int))

