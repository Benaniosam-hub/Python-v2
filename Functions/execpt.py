print("--- Division Game ---")

num1 = input("Enter a number: ")
num2 = input("Enter a number to divide by: ")

try:

    result = float(num1) / float(num2)
    print(f"Success! The answer is: {result}")

except ZeroDivisionError:
    print("Error: You cannot divide a number by zero!")

except ValueError:
    print("Error: Please only type numbers, not letters!")