employees =  ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']

gym_members = ['April', 'John', 'Corey']

developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

user = set(gym_members).symmetric_difference(employees)
print (gym_members)
print(user) 


a = {10, 20, 30, 40}
b = {60, 50}

c = a.difference(b)
print(c)
print(a)
d = a.difference_update(b)
print(d)
print(a)

print(a.issuperset(b))
print(a.isdisjoint(b))
