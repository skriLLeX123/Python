#program to implement functionality of eval function
#The eval() method parses the expression passed to this method and runs python expression (code) within the program.
if __name__=="__main__":
    n=int(input())
    list1=[]
    #storing name of list in a variable so that it can be evaluated as expression
    word="list1."
    for _ in range(n):
        command,*arguments=input().split()
        if command=="print":
            eval(command+"("+word[0:-1]+")")
        else:
            eval(word+command+"("+','.join(arguments)+")")

    
