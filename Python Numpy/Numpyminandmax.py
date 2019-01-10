#program to demonstrate arithmetic operations on  umpy arrays
import numpy
a,b=map(int,input().split())
list1=numpy.array([[int(x) for x in input().split()]for c in range(a)])
mins=numpy.min(list1,axis=1)
maxs=numpy.max(list1,axis=1)
print(mins,maxs,sep="\n")

'''
Sample Input

4 2
1 2
3 4
5 6
7 8

#Sample Ouput

[1 3 5 7]
[2 4 6 8]

'''
