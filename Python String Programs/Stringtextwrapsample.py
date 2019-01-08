#program to represent implementation of textwrap in strings

import textwrap
def merge_the_tools(string, k):
    list1=textwrap.wrap(string,k)
    for item in list1:
        d=""
        for letter in item:
            if letter not in d:
                d+=letter
        print(d)
           

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
