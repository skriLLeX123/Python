#program to demonstrate arithmetic operations on  umpy arrays
import numpy
numpy.set_printoptions(legacy='1.13')
nparray=numpy.array([x for x in input().split()],dtype=float)
print(numpy.floor(nparray),numpy.ceil(nparray),numpy.rint(nparray),sep="\n")

