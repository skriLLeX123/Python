#You are given two integer arrays of size X and X ( &  are rows, and  is the column). Your task is to concatenate the arrays along 0 axis .

'''
Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined:

import numpy

array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print numpy.concatenate((array_1, array_2, array_3))    

#Output
[1 2 3 4 5 6 7 8 9]
If an array has more than one dimension, it is possible to specify the axis along which multiple arrays are concatenated. By default, it is along the first dimension.

import numpy

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print numpy.concatenate((array_1, array_2), axis = 1)   

#Output
[[1 2 3 0 0 0]
 [0 0 0 7 8 9]]
 '''
import numpy
a,b,c=[int(x) for x in input().split()]
n=numpy.array([[int(x) for x in input().split()] for i in range(a)])
m=numpy.array([[int(y) for y in input().split()] for j in range(b)])
print(numpy.concatenate((n,m),axis=0))

'''
Sample Input

4 3 2

1 2
1 2 
1 2
1 2
3 4
3 4
3 4

Sample Output

[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]]
 '''

