#write a program to implement the functionalities of text-alignment methods like rjust(),ljust() and center()
n=7
for i in range(n//2):
    print(('.|.'*i).rjust((n//2)*3,'-')+'.|.'+('.|.'*i).ljust((n//2)*3,'-'))
print(('welcome').center(n*3,'-'))
for i in range(n//2-1,-1,-1):
    print(('.|.'*i).rjust((n//2)*3,'-')+'.|.'+('.|.'*i).ljust((n//2)*3,'-'))


  
