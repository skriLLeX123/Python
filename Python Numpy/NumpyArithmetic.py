#program to demonstrate arithmetic operations on  umpy arrays
import numpy
n,m=map(int,input().split())
a,b=(numpy.array([input().split() for _ in range(n)],dtype=numpy.int)for x in range(2))
print(a+b,a-b,a*b,a//b,a%b,a**b,sep="\n")

