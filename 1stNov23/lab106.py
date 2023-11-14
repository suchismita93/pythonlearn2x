products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Smartphone", "price": 500},
    {"name": "Tablet", "price": 300},
    {"name": "Headphones", "price": 100},
]
print(type(products))
print(type(products[0]))

def is_affordable(item):
   # return item.get('price')<500
    return item['price'] < 500
def is_affordable(n):
    return len(n["name"]) > 4


aff_item=list(filter( is_affordable,products))
aff_name= list(filter(is_affordable,products))
print(aff_item)
print(aff_name)
for i in aff_item:
    print(i["price"],i["name"])
for i in aff_name:
    print(i["price"], i["name"])

