#Write a program that calculates and displays the letter grade for a given numerical score
# (e.g., A, B, C, D, or F) based on the following grading scale:
#input- score - 89
#output- B A: 90-100 B: 80-89 C: 70-79 D: 60-69 F: 0-59
#If, elif, else

score=int(input("Enter the Mark"))
if score>=90 and score<=100:
 print("Grade-A")
elif score>=80 and score<=89:
    print("Grade-B")
elif score>=70 and score<=79:
    print("Grade-C")
elif score>=60 and score<=69:
    print("Grade-D")
elif score>=50 and score<=59:
    print("Grade-F")

#Task 2
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
    #Task 3
    side1 = int(input("Enter the length of side"))
    side2 = int(input("Enter the length of side"))
    side3 = int(input("Enter the length of side"))
    if side1 == side2 == side3:
        print("The triangle is equilateral ")
    elif side1 == side2 and side3 != side1:
        print("The triangle is isosceles  ")
    else:
        print("The triangle is scalene")






