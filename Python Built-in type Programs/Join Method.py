#program to implement join method functionality
if __name__ == '__main__':
    n = int(input("Enter Number: "))

list1=[str(x) for x in range(1,n+1)]

#join method joins the elements of iterable with charachter specifed in single quotation
print(''.join(list1))
    
