'''
Lambda is a single expression anonymous function often used as an inline function.
In simple words, it is a function that has only one line in its body.
It proves very handy in functional and GUI programming.

>> sum = lambda a, b, c: a + b + c
>> sum(1, 2, 3)
6
Note:

Lambda functions cannot use the return statement and can only have a single expression.
Unlike def, which creates a function and assigns it a name, lambda creates a function and returns the function itself.
Lambda can be used inside lists and dictionaries.

'''

import random
import re
import sys
cube = lambda x: x**3 

def fibonacci(n):
    list1=[]
    a=0
    b=1
    while len(list1)<n:
        list1.append(a)
        list1.append(b)
        a=a+b
        b=a+b
    return list1[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

'''
Sample Input

5

Sample Output

[0, 1, 1, 8, 27]

''
