#program to demonstrate arithmetic operations on  umpy arrays
import numpy
import numpy
a,b=map(int,input().strip().split())
n=numpy.array([[int(x) for x in input().split()] for c in range(b)])
nparray=numpy.sum(n,axis=0)
print(nparray.prod())

