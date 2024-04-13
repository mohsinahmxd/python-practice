nums = [1, 7, 4, 44, 33] # creating a list
print(nums[-2])
print(nums[0])
print(nums[0:3])
print(nums[-2:]) # last 2 elements 
print(nums[1:])

nums.append(6) #add to the end
nums.insert(2, 'x') # at index 2, add 'x
print(nums)
nums.remove('x') # remove 'x' - in python it does not leave a gap in the list
print(nums)

print('x' in nums)
print(len(nums))

# other methods
# pop - remove the last element from a list, pop it off
# sort - sort a list, 
# clear - remove all elements from a list