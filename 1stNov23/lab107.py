numList = [30, 2, -15, 17, 9, 100]

def num_greater_10(num):
    return num > 10
greater_10=list(filter( num_greater_10,numList))
print(greater_10)
greater_101=list(filter(lambda n : n >10,numList))
print(greater_101)

numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
def is_even(num):
    return num % 2==0
even_number_tuple= tuple(filter(is_even,numbers_tuple))
print(even_number_tuple)

l = [(1, 23), (34, 34)]
print(l)
print(l[0])
print(l[0] [1])
print(l[0] [0])
