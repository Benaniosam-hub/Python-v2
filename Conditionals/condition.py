'''
score = 100
if score < 0 or score > 100:
    print ("Invalid Mark")
elif score >= 80:
    print("Grade A")
elif score >= 60:
    print("Grade B")
elif score >= 45:
    print("Grade C")
else:
    print("Failed")

user = input("Enter the integer number: ")

if user <= 0:
    user = 0
    print("Negative number changed into zero")
elif user == 0:
    print("Zero")
elif user == 1:
    print("Single")
else: 
    print("More")
'''
"""
x = 0
y = 5

if x < y:
    print ("Yes")

if y:
    print("you are right")

if x or y:
    print ("ya ya")

if 'bena' in 'benaniosam':
    print("True u are right")
else:
    print("Guess again")

if 'sam' in ['ram','dom','boom','sam']:
    print ("Yes he is here")
else:
    print("Nah your wrong")

"""
'''
raining = True
print("Let's go to the", 'beach' if not raining else 'library')

age = 23
s = 'minor' if age < 21 else 'adult'
print(s)

print('yes' if ('am' in ['ram','jam','sam']) else 'no')

a = 1
b = 2
if a > b:
    m = a
else:
    m = b
print(m)

# This can be written by one line:

m = a if a > b else b

points = [(1, 4), (3, 6), (7, 3)]

for x, y in points:
    print(f"{x = } and {y = }")

for i in range (5):
    print(i)


students = {
    "Alice": 89.5,
    "Bob": 76.0,
    "Charlie": 92.3,
    "Diana": 84.7,
    "Ethan": 88.9,
    }

for student in students:
    print(student, "->", students[student])

teams = {
    "Colorado": "Rockies",
    "Chicago": "White Sox",
    "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners",
    }


for b in teams:
    print(b, "->",teams[b])


for team in teams.items():
    print(team)

for team in teams.keys():
    print(team)

for team in teams.values():
    print(team)

'''
a = [1,2,3,4,5,6,7,8]
target = 5

for i in a:
    print(f"Processing..{i}")
    if i == target:
        print(f"Target found..{target}")
        break