'''Removing Elements

Given the list colors = ["red", "blue", "green", "blue", "yellow"]:

Remove the first occurrence of "blue" using .remove().

Remove and print the last item from the list using .pop().'''

colors = ["red", "blue", "green", "blue", "yellow"]

colors.remove("blue")
print("You been removed the last item color: "+ colors.pop(-1))
print(colors)