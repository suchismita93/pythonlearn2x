numbers=[1,-2,-3,-4,5,6,7,-8,9,10]

def is_positive(num):
    return  num > 0

positive_numbers = filter(is_positive,numbers)#filter(function.value)

print(list(positive_numbers))