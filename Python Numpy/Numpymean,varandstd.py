#program to demonstrate mean, variance and standard deviation operations on  numpy arrays
import numpy
numpy.set_printoptions(legacy='1.13')
a,b=map(int,input().split())
nparray=numpy.array([[int(x) for x in input().split()]for i in range(a)])
print(numpy.mean(nparray,axis=1))
print(numpy.var(nparray,axis=0))
print(numpy.std(nparray,axis=None))

'''
Sample Input

2 2

1 2
3 4

Sample Output

[ 1.5  3.5]
[ 1.  1.]
1.11803398875

'''

