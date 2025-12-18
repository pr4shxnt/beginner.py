#3.1 Determining whether a given year is a leap year based on the workflow given


#a using Nested if
year = int(input("Enter a year: "))

if year % 4 == 0:
    print(f"{year} is divisible by 4")
    
    if year % 100 == 0:
        print(f"{year} is divisible by 100")
        
        if year % 400 == 0:
            print(f"{year} is divisible by 400, so the year is a leap year.")
        else:
            print(f"{year} is not divisible by 400, so the year is not a leap year.")
    else:
        print(f"{year} is not divisible by 100. so the year is a leap year.")
else:
    print(f"{year} is not divisible by 4, so the year is not a leap year.")


#b using elif
year2 = int(input("Enter a year: "))

if year % 4 != 0:
    print(f"{year} is not divisible by 4, so the year is not a leap year")

elif year % 100 != 0:
    print(f"{year} is divisible by 4 but not by 100, so the year is a leap year")

elif year % 400 != 0:
    print(f"{year} is divisible by 100 but not by 400, so the year is not a leap year")

else:
    print(f"{year} is divisible by 400, so the year is a leap year")


# c) using conditional statement
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not leap year")
