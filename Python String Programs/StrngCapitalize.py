#program that takes input string and returns string with first letter of each word capitalized

def solve(s):
    return ' '.join([item.capitalize() for item in s.split()])
if __name__=="__main__":
    s=input()
    result=solve(s)
    print(result)
