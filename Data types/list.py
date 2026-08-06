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

supplies = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]
  
camp_site = ["Crystal Lake", 404, 95.5, 10, False]
supplies.remove("tent")
supplies.remove("sleeping bags")
supplies.insert (-1, "toilet paper")
delete = supplies.pop(3)
print (supplies)
print("the item "+ delete +" is deleted")