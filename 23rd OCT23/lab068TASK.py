#Task #2
# Sum of Digits: Create a function that calculates the sum of the digits of a positive integer.
#n = 12345 ,sum = 15 ,n = 123 ,sum = 6
'''digit=12345
mod1=digit % 10
print(mod1)
digit=1234
mod2=digit % 10
print(mod2)
digit=123
mod3=digit % 10
print(mod3)
digit=12
mod4=digit % 10
print(mod4)
digit=1
mod5=digit % 10
print(mod5)
print(mod1+mod2+mod3+mod4+mod5)'''
num=int(input("Enter a num"))
sum=0
while num != 0:
    digit=num % 10 #give reminder
    sum=sum + digit
    num //=10 #num=int(num/10) both are same
print(sum)

