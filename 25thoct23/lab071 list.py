my_list=[1,2,3]
my_list2=[1,True,"suchi"]

print("initial list:",my_list)
#indexing
print("Element at index 0:",my_list[0])
#changing an element
my_list[1]=20
print("List after changing element at index 1:",my_list)
# append()  adding
my_list.append(4)
print("list after appending:",my_list)
# extend()
my_list.extend([5,6])
print("list after extending:",my_list)
# insert()
my_list.insert(1,'a')
print("list after inserting 'a'at index 1:",my_list)
# Remove()
my_list.remove('a')
print("List after removing'a':",my_list)
# copy()
myCOPYLIST=my_list.copy()
print(myCOPYLIST)
#clear()
my_list.clear()
print("initial list:",my_list)
print(myCOPYLIST)
#print("index of 3 in the list:",my_list[3])
print("index of 3 in the list:",myCOPYLIST[3])
myCOPYLIST.sort()
myCOPYLIST.reverse()
print(myCOPYLIST)
print(len(myCOPYLIST))
print(myCOPYLIST[3])
print(myCOPYLIST[5])
print(myCOPYLIST.remove(3))