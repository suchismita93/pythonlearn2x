#1. Write a Python program to find the largest number in a list.
list=[56,89,83,20,56]
# Using sort()
list.sort()
print(list)
print("Largest number of the list :",list[-1])
# using max()
print("Largest number",max(list))


#2. Write a Python program to find the smallest number in a list.
list1=[34,90,67,83,77,12]
print("smallest number",min(list1))
list1.sort()
print(list1)
print("@@smallest number of the list:-",list1[0])

