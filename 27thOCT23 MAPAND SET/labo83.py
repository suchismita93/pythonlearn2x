# list is mutable ,its content  can be changed mylist
my_list=[1,2,3,4,5]
print(my_list)
my_list[1]=20
print(my_list)
print(type(my_list))
# Tuple/ collection items/immutable in nautre/ no modification
car=("Audi","Ford","Audi","Thar")
print(type(car))
#car[1]="FORD"
print(len(car))
#tuple(),its content can't chng
#list[],it's content canbe chnged
#list can be converted to tuple
list1=[1,2,3,3,8,9]
print(tuple(list1))