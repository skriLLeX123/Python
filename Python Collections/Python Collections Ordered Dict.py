
'''
collections.OrderedDict
An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.

Example

Code

>>> from collections import OrderedDict
>>> 
>>> ordinary_dictionary = {}
>>> ordinary_dictionary['a'] = 1
>>> ordinary_dictionary['b'] = 2
>>> ordinary_dictionary['c'] = 3
>>> ordinary_dictionary['d'] = 4
>>> ordinary_dictionary['e'] = 5
>>> 
>>> print ordinary_dictionary
{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
>>> 
>>> ordered_dictionary = OrderedDict()
>>> ordered_dictionary['a'] = 1
>>> ordered_dictionary['b'] = 2
>>> ordered_dictionary['c'] = 3
>>> ordered_dictionary['d'] = 4
>>> ordered_dictionary['e'] = 5
>>> 
>>> print ordered_dictionary
OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
somedict=OrderedDict()
n=int(input())
for i in range(n):
    data=input()
    if data in somedict.keys():
        somedict[data]+=1
    else:
        somedict[data]=1
print('distinct words ',len(somedict.keys()))
print('count of words ',*(somedict.values()))

'''
Sample Input

4
bcdef
abcdefg
bcde
bcdef
Sample Output

3
2 1 1
'''

