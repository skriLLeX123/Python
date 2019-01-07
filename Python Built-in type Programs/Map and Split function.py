#program to implement map and split method functionality
if __name__ == '__main__':

    #split function divides single string into multiple chunks
    #map function maps values of iterable to function specified as first parameter
    list1=list(map(int,input().split()))

    #printing second max number in the list
    print(max([item for item in list1 if item!=max(list1)]))
    
              

    
