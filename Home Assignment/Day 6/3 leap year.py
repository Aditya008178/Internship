#3. Function is_leap(year) returns True if the year is a leap year, else False

def is_leap_year():
    
    year = int(input("Enter the year : "))
    
    if year % 400 == 0 or year % 100 == 0 or year % 4 == 0 :
        print(f"{year} is Leap year  ")
    else : 
        print(f"{year} is  not a Leap year  ")
    
is_leap_year()