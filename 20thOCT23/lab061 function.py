#functions
output=max(1,3) #max() inbuilt function
print(output)
#what is function??
# block of code
#divide into 2 part
# 1-- Built in -which are created by the python guys
# for you so that you can use them without creating your own

# 2--Customer function- you can create a fun which is a block of code ,anyone can reuse it
# fun are reusable --using def() keyword
a=int(input("enter a\n"))
b=a=int(input("enter b\n"))
print(a+b)
#creat a func-def
def sum(a,b):
    return a+b
a=int(input("enter a\n"))
b=a=int(input("enter b\n"))
print(sum(a,b))
print(sum(34,45))
########
print(sum(89,90))
