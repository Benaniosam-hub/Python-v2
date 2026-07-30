words = ["python", "is", "awesome"]
new = []
for i in words:
    caps = i.upper()

print(new)

# LIST COMPREHENSION METHOD

list_new = [i.upper() for i in words]

print (list_new)