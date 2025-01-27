# Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
  count = 0
  
  for i in range(len(nums)):
    if nums[i] == 9:
      count = count + 1
      
  
  return count



# Test Cases

print(array_count9([1, 2, 9])) #→ 1
print(array_count9([1, 9, 9])) #→ 2
print(array_count9([1, 9, 9, 3, 9])) #→ 3