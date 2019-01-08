#program to demonstrate functionality of transpose and flatten functions of numpy module
import numpy
list1=input().strip().split()
x,y=list(map(int,list1))
list2=[input().split() for i in range(x)]
list3=[i for item in list2 for i in item]
nparray=numpy.array(list3,int)
npshapedarray=numpy.reshape(nparray,(x,y))
nptransposearray=numpy.transpose(npshapedarray)
npflattenarray=npshapedarray.flatten()
print(nptransposearray)
print(npflattenarray)
