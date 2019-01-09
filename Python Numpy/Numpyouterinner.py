#The outer tool returns the outer product of two arrays.

import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.outer(A, B)     #Output : [[0 0]
                            #          [3 4]]


The inner tool returns the inner product of two arrays.

import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.inner(A, B)     #Output : 4

#a=[a,b] b=[e,f]
#  [c,d]   [g,h]
#innerproduct=a*e+b*f  a*g+b*h
#             c*e+d*f  c*g+d*h

#a=[a,b] b=[e,f]
#  [c,d]   [g,h]
#cross=a*f-b*e  c*h+d*g


#a=[a,b] b=[e,f]
#  [c,d]   [g,h]
#outer= a*f a*f a*g a*h
#       b*f b*f b*g b*h
#       c*f c*f c*g c*h
#       d*f d*f d*g d*h

import numpy
a=numpy.array([int(x) for x in input().split()])
b=numpy.array([int(x) for x in input().split()])
print(numpy.inner(a,b),numpy.outer(a,b),sep="\n")


