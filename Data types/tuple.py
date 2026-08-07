'''
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (6, 7, 8, 9, 10)
y = ()
for i in tuple1:
    y += (i*2,)
z = ()
for x in tuple2:
    z += (x*3,)

c = y + z

print(c)

'''

list1=["sam","jam","ram"]
list1[0]="chuck"
print(list1)

tup1=("sam","ram","dam")
(employee1,employee2,employee3) = tup1

print(employee1)
print(employee2)
print(employee3)
