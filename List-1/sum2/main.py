# Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.

# Version 1 (My Attempt - using while loop)
def sum2(nums):
  if not nums:
    return 0

  sum = 0
  index = 0

  while index < 2 and index < len(nums):
    sum += nums[index]
    index += 1

  return sum

# Version 2 (My Second Attempt)
def sum2(nums):
  if not nums:
    return 0

  return sum(nums[:2])

# Version 3 (Optimized)
def sum2(nums):
  return sum(nums[:2])

# Version 4 (Using a for loop)
def sum2(nums):
  sum = 0
  for i in range(min(2, len(nums))):
    sum += nums[i]
  return sum

if __name__ == "__main__":
    # Example test cases
    print(sum2([1, 2, 3]))  # Output: 3
    print(sum2([1, 1]))  # Output: 2
    print(sum2([1, 1, 1, 1]))  # Output: 2
    print(sum2([1, 2]))  # Output: 3
    print(sum2([1]))  # Output: 1
    print(sum2([]))  # Output: 0
    print(sum2([4, 5, 6]))  # Output: 9
    print(sum2([4]))  # Output: 4
