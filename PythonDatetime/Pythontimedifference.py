import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    fmt="%a %d %b %Y %H:%M:%S %z"
    tt1=datetime.strptime(t1,fmt)
    tt2=datetime.strptime(t2,fmt)
    return str(int(abs((tt1-tt2).total_seconds())))

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        print(delta)

'''
Sample input

2

Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000

Sample output

25200

Sample input

Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000

Sample output

88200

''
