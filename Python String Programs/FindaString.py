#write a program to find number of occurences of substring in the particular string

def count_substring(string, sub_string):
    #count function is used to count the substring in the given string. it takes three parameters substring,start_index,end_index
    return sum([string.count(sub_string,0+i,len(sub_string)+i) for i in range(len(string)+1)])


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()    
    count = count_substring(string, sub_string)
    print(count)
  
