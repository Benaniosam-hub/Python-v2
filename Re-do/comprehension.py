words = ["python", "is", "awesome"]
new = []
for i in words:
    caps = i.upper()

print(new)

# LIST COMPREHENSION METHOD

list_new = [i.upper() for i in words]

print (list_new)

# String Lengths:

fruits= ["apple","banana","kiwi","cherry"]

list_2 = [len(x) for x in fruits]

print(list_2)

# If-Else Inline Transformation:

scores = [45, 80, 62, 30, 95]

new_list = ["pass" if y >= 60 else "fail" for y in scores]

print(new_list)
