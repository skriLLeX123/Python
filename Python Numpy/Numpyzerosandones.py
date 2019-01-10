#program to demonstrate functionality of zeros and ones functions of numpy module
import numpy
list1=input().strip().split()
tuple1=tuple([int(x) for x in list1])
print(numpy.zeros(tuple1,dtype=numpy.int))
print(numpy.ones(tuple1,dtype=numpy.int))

'''
Sample Input 0

3 3 3

#first 3 is for number of arrays to be printed, second 3 is for number of rows in each array
and third 3 is for number of columns in each array

Sample Output 0

[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]

'''
