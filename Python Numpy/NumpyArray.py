# program to convert given list into array and using numpy module and reverse the array
import numpy

def arrays(arr):
    return numpy.array(arr[::-1],float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
