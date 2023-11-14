# Map and Filter in the list
sq= lambda x:x*x
#result=sq(5)
#print(result)

#  Map function(where we will go from one item and apply a function)
num=[1,2,3,4,5]
#sq_num=[1,4,9,16,25]
sq_num=[]
for i in num:
    sq_num.append(sq(i))

print(sq_num)
#Map function
sq_num2 = list(map(lambda x:x*x,num))
print("#####",sq_num2)

def triple(a):
    return a * 3

sq_num3 = list(map(triple,num))
print("#####",sq_num3)

