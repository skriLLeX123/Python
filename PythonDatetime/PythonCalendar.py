# Program to print weekday for particular date

import calendar
a=[int(x) for x in input().split()]
a=calendar.weekday(a[2],a[0],a[1])
print(calendar.day_name[a].upper())

'''
Sample Input

08 05 2015
Sample Output

WEDNESDAY
'''
