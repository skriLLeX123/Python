#write a program to check whether charachters in string are number, alphanumber, lowercase, uppercase, alphabetic

if __name__ == "__main__":
    s=input()
    print(any(e.isalnum() for e in s))
    print(any(e.isalpha() for e in s))
    print(any(e.isdigit() for e in s))
    print(any(e.islower() for e in s))
    print(any(e.isupper() for e in s))





  
