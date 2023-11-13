#factorial
#loop
#n=5
#5!---5*4*3*2*1--120
#4=====4*3*2*1==6
n=int(input("Enter a number"))
if  n<0:
    print("factorial is not possible !!!")
else:
    fact=1
    for i in range(1,n+1): #(0,len-1)
        fact=fact * i

print("fact is-->",fact)
