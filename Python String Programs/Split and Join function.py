#program to implement the functionality of split and join function

def split_and_join(s):
    
    #split function splits the words in string and stores in list
    newlist=s.split(" ")
    
    #join function joins the elements in list using charachter specified in single quotation
    new_string="-".join(newlist)
    return new_string
    

if __name__=="__main__":
    s=input()
    result=split_and_join(s)
    print(result)
