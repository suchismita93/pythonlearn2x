t=("The TestingAcademy","for","The TestingAcademy")
print("\nSet with the use of Tuple:")
print(set(t))

set1={1,2,3,}
set2={4,5,6}
my_set=set1.union(set2)
print(my_set)

set={1,2,3,4,6}
set3={4,5,6,7}
my_set2=set.intersection(set3)
print("@@",my_set2)

set={1,2,3,4,6}
set3={4,5,6,7}
my_set3= set.difference(set3)
my_set3= set3.difference(set)
print("!!!",my_set3)

set={1,2,3,4}
set3={4,3}
subset= set3.issubset(set)
print("!!!",subset)

set={1,2,3,4,6}
set3={4,5,6,7}
set3.remove(5)
print("@@@@",set3)