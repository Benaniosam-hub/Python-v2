#one.py
def my_func():
    print ("Hello im here.")

try:
    a,b = 6,'7'
    c = a+b
    print (c)

except TypeError:
    print("Type error")

finally:
    print("Anyways its error lets move on")

def ask_for_number():
    try:
        r = int(input("enter number: "))
    except:
        print("Enter number gang")
    finally:
        print("End of try/except/finally")