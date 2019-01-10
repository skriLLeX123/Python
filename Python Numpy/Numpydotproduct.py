#program to demonstrate arithmetic operations on  umpy arrays
import numpy
c=int(input())
a=numpy.array([[int(x) for x in input().split()]for i in range(c)])
b=numpy.array([[int(x) for x in input().split()]for i in range(c)])
print(numpy.dot(a,b))


#Sample Input
#2

#1 2
#3 4

#1 2
#3 4

#Sample Output
#[[ 7 10]
# [15 22]]


