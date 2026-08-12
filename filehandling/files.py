names = input("Enter your name: ")

file = open("names.txt","a")
file.write(f"{names}\n")
file.close()
