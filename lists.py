nums = [1, 7, 4, 44, 33]
print(nums[-2])
print(nums[0])
print(nums[0:3])
print(nums[-2:]) # last 2 elements
print(nums[1:])

nums.append(6)
nums.insert(2, 'x')
print(nums)
nums.remove('x')
print(nums)

print('x' in nums)
print(len(nums))
