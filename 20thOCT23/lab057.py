#fabonaci series-----n=7
#0+1,1+1,1+2,2+3,3+5,5+8
number=int(input("Enter a number\n"))
a,b=0,1
while(a<number):
    print(a,end=' ')
    a,b=b,a+b
