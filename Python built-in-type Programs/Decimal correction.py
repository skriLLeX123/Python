#program to pring average of students with decimal correction of upto 2 places

if __name__ == '__main__':
    n = int(input("Enter no of students: "))
    
    #creating empty dictionary to store name as keys and average of scores as value of that key
    student_marks = {}

    for _ in range(n):
        name,*scorelist=input().split(' ')
        student_marks[name]=f'{sum([float(score) for score in scorelist])/len(scorelist):.2f}'
    print(student_marks[input()])
    
              

    
