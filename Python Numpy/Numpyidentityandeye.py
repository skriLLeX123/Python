#program to demonstrate functionality of identity and eye functions of numpy module
import numpy
#print(numpy.identity(3))
#print(numpy.eye(8, 7, k = -1,dtype=numpy.int))
#Diagonal we require; k>0 means diagonal above main diagonal or vice versa.
numpy.set_printoptions(legacy='1.13')
list1=input().strip().split()
tuple1=tuple([int(x) for x in list1])
print(numpy.eye(*tuple1,k=0))


#Sample Input
 #  4 5

#Sample Output
#    [[ 1.  0.  0.  0.  0.]
#    [ 0.  1.  0.  0.  0.]
#    [ 0.  0.  1.  0.  0.]
#    [ 0.  0.  0.  1.  0.]]
