# Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.

# Version 1 (My Attempt)
def max_end3(nums):
  max_int = max(nums[0], nums[len(nums)-1])
  output = []

  for i in range(len(nums)):
    output.append(max_int)

  return output

# Version 2 (Optimized)
def max_end3(nums):
  max_int = max(nums[0], nums[len(nums)-1])
  return [max_int] * len(nums)

if __name__ == "__main__":
    # Example test cases
    print(max_end3([1, 2, 3]))  # Output: [3, 3, 3]
    print(max_end3([11, 5, 9]))  # Output: [11, 11, 11]
    print(max_end3([2, 11, 3]))  # Output: [3, 3, 3]
    print(max_end3([11, 3, 3]))  # Output: [11, 11, 11]
    print(max_end3([3, 11, 11]))  # Output: [11, 11, 11]
    print(max_end3([2, 2, 2]))  # Output: [2, 2, 2]
    print(max_end3([2, 11, 2]))  # Output: [2, 2, 2]
    print(max_end3([0, 0, 1]))  # Output: [1, 1, 1]

