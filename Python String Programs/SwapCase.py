#swap the case of letters from lower to upper and vice versa

def swap_case(s):
    new_string=""
    for letter in s:
        if letter==letter.lower():
            new_string+=letter.upper()
        else:
            new_string+=letter.lower()
    return new_string

if __name__=="__main__":
    s=input()
    result=swap_case(s)
    print(result)
