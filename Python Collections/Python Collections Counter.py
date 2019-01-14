
''' collections.Counter() 
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
Sample Code

>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
list1=list(map(int,input().split()))
m=int(input())
list2=[list(map(int,input().split())) for x in range(m)]
from collections import Counter
cost=0
for item in list2:
    if item[0] in list1:
        list1.remove(item[0])
        cost+=item[1]
print(cost)

'''
Sample Input

10

2 3 4 5 6 8 7 6 5 18

6

6 55
6 45
6 55
4 40
18 60
10 50


Sample Output

200
'''
    
