#program to demonstrate arithmetic operations on  umpy arrays
import numpy
a,b=map(int,input().split())
list1=numpy.array([[int(x) for x in input().split()]for c in range(a)])
mins=numpy.min(list1,axis=1)
print(numpy.max(mins))

