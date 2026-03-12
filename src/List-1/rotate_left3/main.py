# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

# Version 1 (My Attempt)
def rotate_left3(nums):
  output = []

  for index in range(0, len(nums)-1):
    curr_num = nums[index + 1]
    output.append(curr_num)

  output.append(nums[0])
  return output

# Version 2 (Optimized)
def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]

# Version 3 (Using Slicing)
def rotate_left3(nums):
  return nums[1:] + nums[:1]

# Version 4 (Version 1 Optimized)
def rotate_left3(nums):
  output = []

  for index in range(1, len(nums)):
    curr_num = nums[index]
    output.append(curr_num)

  output.append(nums[0])
  return output

# Version 5 (Using a while and for loop)
def rotate_left3(nums):
  output = []
  index = 1

  while index < len(nums):
    curr_num = nums[index]
    output.append(curr_num)
    index += 1

  output.append(nums[0])
  return output

if __name__ == "__main__":
    # Example test cases
    print(rotate_left3([1, 2, 3]))  # Output: [2, 3, 1]
    print(rotate_left3([5, 11, 9]))  # Output: [11, 9, 5]
    print(rotate_left3([7, 0, 0]))  # Output: [0, 0, 7]
    print(rotate_left3([1, 2, 1]))  # Output: [2, 1, 1]
    print(rotate_left3([0, 0, 1]))  # Output: [0, 1, 0]
