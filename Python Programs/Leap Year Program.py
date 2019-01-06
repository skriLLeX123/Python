def is_leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return "Leap Year"
            else:
                return "Common Year"
        else:
            return "Leap Year"
    else:
        return "Common Year"


year=int(input("Enter Year: "))
print(is_leap(year))

