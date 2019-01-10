#program to demonstrate arithmetic operations on  umpy arrays
import numpy
n,m=map(int,input().split())
a,b=(numpy.array([input().split() for _ in range(n)],dtype=numpy.int)for x in range(2))
print(a+b,a-b,a*b,a//b,a%b,a**b,sep="\n")

'''
Sample Input

1 4
1 2 3 4
5 6 7 8
Sample Output

[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]]
'''
