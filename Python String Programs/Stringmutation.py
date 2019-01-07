#swap the case of letters from lower to upper and vice versa

def mutate_string(s,n,c):
    new_string=s[:n]+c+s[n+1:]
    return new_string
#another approach
#  newstring="";
#    for i in range(len(string)):
#       if i==position:
#           newstring+=character;
#       else:
#          newstring+=string[i]
#  return newstring
    


if __name__=="__main__":
    s=input()
    l,c=input().split()
    s_new=mutate_string(s,int(l),c)
    print(s_new)
  
