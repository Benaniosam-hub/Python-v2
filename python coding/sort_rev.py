'''Given the list scores = [88, 42, 95, 70, 100, 63]:

Sort the list in ascending order

Reverse the list in-place so it is sorted in descending order.'''

scores =[88, 42, 95, 70, 100, 63]
scores.sort()
print(scores)
new=scores.copy()
new.reverse()
print(new)