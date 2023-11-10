#2 Task
#Calculate the area of a circle
Radius=int(input("Enter radius \n"))
area=float(3.14*Radius**2)
print(area)

#Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
#Use the ternary operator to find the maximum of three numbers entered by the user. [on_true] if [expression] else [on_false]
num1=int(input("Enter num1"))
num2=int(input("Enter num2"))
result1="Greater than" if num1>num2 else "less than"if num1<num2 else "equal to"
print(f"num1 :{result1} num2")
# OR
a=int(input("Enter number1"))
b=int(input("Enter number2"))
if(a>b):
    print(f"{a} is greater than{b}")
elif(a<b):
    print(f"{a} is less than {b}")
else:
    print(f"{a} is equal to {b}")

    # Calculates the square and cube of a given number.
num = int(input("Enter number"))
square = num ** 2
cube = num ** 3
print(f"Square is:{square}\nCube is:{cube}")
print("Square is", square, "Cube is", cube)

