list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
y = []
for i in list1:
    y.append(i*2)
z = []
for x in list2:
    z.append(x*3)

c = y + z

print(c)