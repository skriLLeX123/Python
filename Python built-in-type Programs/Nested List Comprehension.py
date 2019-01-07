#Program to print name of students with second lowest grades
if __name__=="__main__":
    #input for number of students
    n=int(input("Enter Number of students: "))

    #list to store name and score of students
    scorelist=[[input("Enter Name: "),float(input("Enter Score: "))] for x in range(n)]

    #calculating lowest grade in list
    lowest_grade=min([sublist[1] for sublist in scorelist])

    #calculating second lowest grade in list
    second_lowest_grade=min([sublist[1] for sublist in scorelist if sublist[1]!=lowest_grade])

    #printing names of students with second lowest grade
    print(*sorted([sublist[0] for sublist in scorelist if sublist[1]==second_lowest_grade]),sep="\n")
    
   

