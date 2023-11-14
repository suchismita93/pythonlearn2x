numbers=[1,2,3,4,5,6,7,8,9,10]
#even_numbers=[2,4,6,8,10]
#filter->number of elements can be less or equal the list
#filter->number of element can be less or equal the list

def is_even(num):
    return  num % 2==0

even_numbers = filter(is_even,numbers)#filter(function.value)

print(list(even_numbers))



