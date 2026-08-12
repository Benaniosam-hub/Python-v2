'''
number = 5
while number > 0:
   
    number -= 1

while True:
    name = input("Enter your name: ")
    if name != "":
        break
'''
'''
phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end=" ")
'''

import random
import time

def read_temperature():
    return random.uniform(20.0,30.0)

while True:
    temperature = read_temperature()
    print(f"Temperature: {temperature:.2f}celsius")

    if temperature >=28:
        print("Required temperature reached! Stopping monitoring.")
        break
    time.sleep(1)