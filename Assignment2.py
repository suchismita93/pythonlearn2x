''''Task #2

✅ Leap Year Checker:
Create a program that determines whether a given year is a leap year.
A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
Use an if-else statement to make this determination.
Input = 2024
Output = Leap year'''

year=int(input("Enter year"))
# not divided by 100 means a leap year
# century year divided by 4 is leap year
if (year % 4 == 0) and (year % 100 != 0):
    print("leap year".format(year))
# year divided by 400 is a leap year
elif (year % 400 ==0) :
    print("leap year".format(year))

# if not divided by both 400 (century year)
# year is not leap year
else:
    print("Not a leap year".format(year))