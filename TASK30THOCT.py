#Find the maximum and minimum elements in a tuple.
my_tuple = (15, 8, 25, 36, 42, 10)
print(max(my_tuple))
print(min(my_tuple))

#Program 2:
#Find the intersection and union of two sets.
set1 = {1, 2, 3, 4, 5}

set2 = {3, 4, 5, 6, 7}
print("set1 U set2:",set1.union(set2))
print("set1 n Set2 :",set1.intersection(set2))

#Program 3:
#Remove duplicate elements from a list.

my_list = [1, 2, 2, 3, 4, 4, 5]
result=list(set(my_list))
print(result)

#Program 4:

my_dict={"name":'suchi','age':23,'address': 'mumbai'}
print(type(my_dict))
#Remove a key-value pair from the dictionary.
op=my_dict.pop('address')
print(my_dict)

#Program 5:
#Convert to Dict JSON Response and Print and Booking Id AND checkin and Checkout Data

a={"bookingid": 2384,

"booking": {

"firstname": "PRAMOD",

"lastname": "Dutta",

"totalprice": 432,

"depositpaid": False,

"bookingdates": {

"checkin": "2022-01-01",

"checkout": "2022-01-01"

},

"additionalneeds": "Lunch"

}

}
print(a)
print(type(a))
print(a["bookingid"],["checkin"])
print(a.get("checkout"))







