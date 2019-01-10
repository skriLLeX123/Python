#program to demonstrate arithmetic operations on  umpy arrays
import numpy
a,b=map(int,input().strip().split())
n=numpy.array([[int(x) for x in input().split()] for c in range(b)])
sumarray=numpy.sum(n,axis=0)
prodarray=numpy.prod(n,axis=1)
print(sumarray)
print(prodarray)

'''
Sample Input

2 2

1 2
3 4

Sample output

[4 6]

[ 2 12]

'''

