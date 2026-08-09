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
