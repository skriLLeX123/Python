#program to demonstrate arithmetic operations on  umpy arrays
import numpy
numpy.set_printoptions(legacy='1.13')
nparray=numpy.array([x for x in input().split()],dtype=float)
print(numpy.floor(nparray),numpy.ceil(nparray),numpy.rint(nparray),sep="\n")

#Sampe Input
#1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

#Sample Ouput
#numpy.floor()-> [ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
#numpy.ceil()->  [  2.   3.   4.   5.   6.   7.   8.   9.  10.]
#numpy.rint()->  [  1.   2.   3.   4.   6.   7.   8.   9.  10.]
