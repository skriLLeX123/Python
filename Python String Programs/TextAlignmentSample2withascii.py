#program to implement functionality of Text alignment module and string.ascii
import string
if __name__=="__main__":
    n=int(input())
    n=5
    L=[]
    for i in range(n):
        s='-'.join(string.ascii_lowercase[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3,'-'))
    print('\n'.join(L[:0:-1]+L))
    
 
