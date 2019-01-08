#program to demonstrate functionality of shape and reshape functions of numpy module
import numpy
arr=input().strip().split()
ndarray=numpy.array(arr,int)
print(numpy.shape(ndarray)) #1 dimensional array : prints number of elements in array
reshaped_array=numpy.reshape(ndarray,(3,3))#reshape function is used to change the shape of array i.e change the number of rows and columns
print(reshaped_array)
print(numpy.shape(reshaped_array))# n dimensional array : prints number of rows and columns
