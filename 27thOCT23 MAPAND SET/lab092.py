list1=[10,20,30,40]
tuple=(10,20,30,40)

def mul_by10(mylist):
    mylist[0] *= 10
    mylist[1] *= 10
    mylist[2] *= 10
print(list1)
mul_by10(list1)
mul_by10(tuple)
print(tuple)  # not assign (immutable)
print(list1)

