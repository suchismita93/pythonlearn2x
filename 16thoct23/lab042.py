#find the maxinum number of 3 number using the ternary optr
num1=int(input("Enter 1st number"))
num2=int(input("Enter 2nd number"))
num3=float(input("Enter 3rd number"))
max_num=num1 if(num1>num2 and num1>num3 )else (num2 if num2>num3 else num3)
print(f"the maximum of {num1},{num2},and {num3} is:{max_num}")

4
