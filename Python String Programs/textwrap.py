#write a program to implement the functionalities of textwrap methods like fill() and wrap()
import textwrap
if __name__=="__main__":
    s="The textwrap module can be used to format text for output in situations\
        where pretty-printing is desired.  It offers programmatic functionality similar\
        to the paragraph wrapping or filling features found in many text editors."
    #wrap method of textwrap module wraps the text within the width specified as second parameter and stores the result in list
    list1=textwrap.wrap(s,width=50)
    for item in list1:
        print(item)

    #fill method of textwrap works in similar fashion as that of wrap method but it stores the result in string format
    somestring=textwrap.fill(s,width=50)
    print(somestring)



  
