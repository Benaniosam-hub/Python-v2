'''
Given a list of integers nums,
create a new list ans that is formed by joining nums with itself 
(repeating the list twice).'''

nums = [1,2,3]
ans = nums + nums
print (ans)

'''Problem:
Given a list of scores, 
find the second highest score (the runner-up). 
Keep in mind that the maximum score might 
appear more than once in the list.
'''
scores = [2,3,6,6,5]
print(f"scores = {scores}")
new_scores = list(set(scores))
new_scores.sort()
new_scores.reverse()
high = new_scores[1]
print(f"The second highest score is: {high}")

 
