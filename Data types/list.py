"""
Core Characteristics of Python Lists:

- Ordered sequence of elements
- Mutable (can be modified after creation)
- Indexed (values can be accessed using index)
- Duplicates allowed
- Used as list comprehensions and for loops

sort() only works on lists where
sorted() works on any iterable object like lists, tuples, dictionaries, etc.
"""
from operator import itemgetter
supplies = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]
  
camp_site = ["Crystal Lake", 404, 95.5, 10, False]
supplies.remove("tent")
supplies.remove("sleeping bags")
supplies.insert (-1, "toilet paper")
delete = supplies.pop(3)
print (supplies)
print("the item "+ delete +" is deleted")
camp_site.extend(["sam","eam"])
print(camp_site)

list5 = [1,2,3,4,5,6,7,8,6,6,9,10]
list5.copy()
counting=list5.count(6)
print(counting)
new_value = list5.index(6,4,6)

product = [{"name":"Shirt", "price": 25}, {"name":"Shoe", "price": 50}, {"name":"Pants", "price": 10}]
product.sort(key=itemgetter("price"))
print(product)

print(new_value)