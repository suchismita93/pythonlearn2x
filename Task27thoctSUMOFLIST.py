#3. Sum all numbers in a list.

list2=[11,22,33,11]
total=sum(list2)
print(total)

#  Method 2
def sum_list():
  sum=0
  for i in list2:
    sum=sum+i
    return sum

print("sum of items in a list:",sum_list())



