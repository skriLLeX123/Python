# program to implement Regex Module
import re
for i in range(int(input())):
    try:
        print(bool(re.compile(input())))
    except:
        print(False)
