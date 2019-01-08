#program to count strings starting with vowels and consonant in a given string and deciding the winner
def minion_game(string):
    string=string.lower()
    dict1={}
    dict2={}
    vowels=['a','e','i','o','u']
    vcounter=0;
    ccounter=0;
    for index in range(len(string)):
        if string[index] in vowels:
            vcounter+=(len(string)-index)
        else:
            ccounter+=(len(string)-index)
    
    
    if vcounter<ccounter:
        print("Stuart",ccounter)
    elif vcounter==ccounter:
        print("Draw")
    else:
        print("Kevin",vcounter)
        


if __name__ == '__main__':
    s = input()
    minion_game(s)
