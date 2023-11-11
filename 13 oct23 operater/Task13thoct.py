 #1 task
# difference between the = operator and the == operator in Python.
a ,b="suchi",10
a=b
print(b)# = is assigns values from right side operands to left side operands
x,y=10,8
print(x==y) # == (Equal opreater)checks the values of two operands are equal nor not
#if the values are same ,retuns True or False

# ** operator do and how is it used?
a1,b1=2,3
num3=a1**b1 # ** is a exponentiation operater
print(num3) # a ** b is a raised to the b power

# ^ is bitwise xor operater=Results bit 1,if any of the operand bit is 1 but not both,otherwiseresults bit 0.
p,q=8,3   #Example=1000   8 (binary)
                # 0011   3 (binary)       .
                # 0011   3 (binary)
                #  ----   APPLY XOR ('vertically')
print(p ^ q)    #1011   result = 11 (binary)
